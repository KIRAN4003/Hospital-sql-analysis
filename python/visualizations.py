import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to MySQL
engine = create_engine(
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_NAME')}"
)

sns.set_style('darkgrid')
plt.rcParams['figure.figsize'] = (12, 5)

# Chart 1 — Medical Conditions by Patient Volume
query1 = """
SELECT medical_condition, COUNT(*) as patient_count
FROM admissions
GROUP BY medical_condition
ORDER BY patient_count DESC
"""
df1 = pd.read_sql(query1, engine)

plt.figure(figsize=(12, 5))
bars = plt.bar(df1['medical_condition'], df1['patient_count'], color='steelblue')
for bar, val in zip(bars, df1['patient_count']):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 50,
             f'{val:,}', ha='center', fontweight='bold')
plt.title('Patient Volume by Medical Condition', fontsize=16, fontweight='bold')
plt.xlabel('Medical Condition')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.savefig('../screenshots/viz_01_conditions.png', dpi=150)
plt.show()
print("Chart 1 saved ✅")

# Chart 2 — Insurance Revenue
query2 = """
SELECT insurance_provider,
       ROUND(SUM(billing_amount), 2) as total_revenue
FROM billing
GROUP BY insurance_provider
ORDER BY total_revenue DESC
"""
df2 = pd.read_sql(query2, engine)

plt.figure(figsize=(12, 5))
bars = plt.barh(df2['insurance_provider'], df2['total_revenue'], color='mediumseagreen')
for bar, val in zip(bars, df2['total_revenue']):
    plt.text(bar.get_width() + 1000000,
             bar.get_y() + bar.get_height()/2,
             f'${val/1e6:.1f}M', va='center', fontweight='bold')
plt.title('Revenue by Insurance Provider', fontsize=16, fontweight='bold')
plt.xlabel('Total Revenue ($)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('../screenshots/viz_02_insurance.png', dpi=150)
plt.show()
print("Chart 2 saved ✅")

# Chart 3 — Monthly Admissions Trend
query3 = """
SELECT 
    admission_month_name,
    admission_month,
    COUNT(*) as admissions
FROM admissions
GROUP BY admission_month_name, admission_month
ORDER BY admission_month
"""
df3 = pd.read_sql(query3, engine)

plt.figure(figsize=(14, 5))
plt.plot(df3['admission_month_name'], df3['admissions'],
         marker='o', color='coral', linewidth=2.5, markersize=8)
plt.fill_between(range(len(df3)), df3['admissions'],
                 alpha=0.1, color='coral')
plt.xticks(range(len(df3)), df3['admission_month_name'], rotation=45, ha='right')
plt.title('Monthly Admissions Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Number of Admissions')
plt.tight_layout()
plt.savefig('../screenshots/viz_03_monthly_trend.png', dpi=150)
plt.show()
print("Chart 3 saved ✅")

# Chart 4 — Admission Type Distribution
query4 = """
SELECT a.admission_type,
       COUNT(*) as count,
       ROUND(SUM(b.billing_amount), 2) as revenue
FROM admissions a
JOIN billing b ON a.patient_id = b.patient_id
GROUP BY a.admission_type
"""
df4 = pd.read_sql(query4, engine)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pie chart
axes[0].pie(df4['count'],
            labels=df4['admission_type'],
            autopct='%1.1f%%',
            colors=['steelblue','coral','mediumseagreen'],
            startangle=140)
axes[0].set_title('Admission Type Distribution',
                   fontsize=14, fontweight='bold')

# Bar chart
bars = axes[1].bar(df4['admission_type'],
                   df4['revenue']/1e6,
                   color=['steelblue','coral','mediumseagreen'])
for bar, val in zip(bars, df4['revenue']/1e6):
    axes[1].text(bar.get_x() + bar.get_width()/2,
                 bar.get_height() + 0.5,
                 f'${val:.1f}M', ha='center', fontweight='bold')
axes[1].set_title('Revenue by Admission Type',
                   fontsize=14, fontweight='bold')
axes[1].set_ylabel('Revenue ($M)')

plt.tight_layout()
plt.savefig('../screenshots/viz_04_admission_type.png', dpi=150)
plt.show()
print("Chart 4 saved ✅")

print("\n✅ All 4 visualizations saved!")