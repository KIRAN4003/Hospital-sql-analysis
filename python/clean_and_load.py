import pandas as pd
from sqlalchemy import create_engine, text

from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_USER     = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST     = os.getenv("MYSQL_HOST")
MYSQL_DB       = os.getenv("MYSQL_DB")
# ============================================================

# ── Step 1: Connect to MySQL ─────────────
print("Connecting to MySQL...")
try:
    engine = create_engine(
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}",
        echo=False
    )
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Connected to MySQL successfully!")
except Exception as e:
    print(f" Connection failed: {e}")
    print("\nCheck your MYSQL_USER and MYSQL_PASSWORD at the top of this file.")
    exit()

# ── Step 2:
df = pd.read_csv("../data/raw/healthcare_dataset.csv")
print(f"✅ Loaded {len(df):,} rows")

# ── Step 3:EDA & Cleaning
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
print("✅ Column names cleaned:", df.columns.tolist())

# ── Step 4: Rename columns for clarity ──────────────────────
df.rename(columns={
    "name"              : "patient_name",
    "blood_type"        : "blood_type",
    "medical_condition" : "medical_condition",
    "date_of_admission" : "date_of_admission",
    "doctor"            : "doctor_name",
    "hospital"          : "hospital_name",
    "insurance_provider": "insurance_provider",
    "billing_amount"    : "billing_amount",
    "room_number"       : "room_number",
    "admission_type"    : "admission_type",
    "discharge_date"    : "discharge_date",
    "medication"        : "medication",
    "test_results"      : "test_results",
}, inplace=True)

# ── Step 5: Fix data types ────────────────────────────────────
df["date_of_admission"] = pd.to_datetime(df["date_of_admission"], errors="coerce")
df["discharge_date"]    = pd.to_datetime(df["discharge_date"],    errors="coerce")
df["billing_amount"]    = pd.to_numeric(df["billing_amount"],     errors="coerce").round(2)
df["age"]               = pd.to_numeric(df["age"],                errors="coerce")

# ── Step 6:Feature engineering ────────────
# Length of stay in days
df["length_of_stay"] = (df["discharge_date"] - df["date_of_admission"]).dt.days

# Age group buckets
bins   = [0, 18, 35, 50, 65, 120]
labels = ["0-18", "19-35", "36-50", "51-65", "65+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

# Admission year and month (for time analysis)
df["admission_year"]       = df["date_of_admission"].dt.year
df["admission_month"]      = df["date_of_admission"].dt.month
df["admission_month_name"] = df["date_of_admission"].dt.strftime("%B")

# Add a clean patient_id
df.insert(0, "patient_id", range(1, len(df) + 1))

# ── Step 7: Clean text values ─────────────────────────────────
text_cols = ["patient_name", "gender", "blood_type", "medical_condition",
             "doctor_name", "hospital_name", "insurance_provider",
             "admission_type", "medication", "test_results"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# ── Step 8: Remove bad rows ───────────────────────────────────
before = len(df)
df = df.dropna(subset=["date_of_admission", "discharge_date", "billing_amount"])
df = df[df["length_of_stay"] >= 0]
df = df[(df["age"] >= 0) & (df["age"] <= 120)]
df = df.drop_duplicates()
print(f"✅ Removed {before - len(df)} bad/duplicate rows")
print(f"✅ Final clean dataset: {len(df):,} rows")

# ── Step 9: Save cleaned CSV ──────────────────────────────────
import os
os.makedirs("../data/cleaned", exist_ok=True)
df.to_csv("../data/cleaned/patients_billing_cleaned.csv", index=False)
print("✅ Cleaned CSV saved to data/cleaned/")

# ── Step 10: Load into MySQL ──────────────────────────────────
print("\nLoading into MySQL...")

# We'll create 3 clean tables from this one CSV:

# TABLE 1: patients (demographic info only)
patients_df = df[[
    "patient_id", "patient_name", "age", "age_group",
    "gender", "blood_type"
]].copy()
patients_df.to_sql("patients", con=engine, if_exists="replace", index=False)
print(f"✅ patients table loaded — {len(patients_df):,} rows")

# TABLE 2: admissions (clinical info)
admissions_df = df[[
    "patient_id", "medical_condition", "doctor_name", "hospital_name",
    "room_number", "admission_type", "medication", "test_results",
    "date_of_admission", "discharge_date", "length_of_stay",
    "admission_year", "admission_month", "admission_month_name"
]].copy()
admissions_df.insert(0, "admission_id", range(1, len(admissions_df) + 1))
admissions_df.to_sql("admissions", con=engine, if_exists="replace", index=False)
print(f"✅ admissions table loaded — {len(admissions_df):,} rows")

# TABLE 3: billing (financial info)
billing_df = df[[
    "patient_id", "insurance_provider", "billing_amount"
]].copy()
billing_df.insert(0, "bill_id", range(1, len(billing_df) + 1))
billing_df["admission_id"] = range(1, len(billing_df) + 1)
billing_df["payment_mode"] = billing_df["insurance_provider"].apply(
    lambda x: "Cash" if x.lower() in ["none", "nan", ""] else "Insurance"
)
billing_df.to_sql("billing", con=engine, if_exists="replace", index=False)
print(f"✅ billing table loaded — {len(billing_df):,} rows")

# ── Step 11: Quick verification ───────────────────────────────
print("\n========== VERIFICATION ==========")
with engine.connect() as conn:
    for table in ["patients", "admissions", "billing"]:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
        count = result.fetchone()[0]
        print(f"  {table:12s} → {count:,} rows in MySQL")

print("\n🎉 All Done next we proceed with sql analysis!")