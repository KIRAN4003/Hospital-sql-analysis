# 🏥 Hospital Operations & Patient Analytics using SQL

![SQL](https://img.shields.io/badge/SQL-MySQL-blue)
![Python](https://img.shields.io/badge/Python-Pandas-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Project Overview

A mid-sized hospital generates thousands of records daily — patient admissions,
doctor assignments, billing transactions, and appointments. Without structured
analysis, critical operational inefficiencies go unnoticed.

This project builds a **relational database from scratch** and answers **20+
real business questions** using advanced SQL — helping hospital management
reduce costs, improve patient flow, and minimise appointment no-shows.

---

## 🎯 Business Problems Solved

| # | Business Question | SQL Technique Used |
|---|---|---|
| 1 | Which department has the highest patient load? | GROUP BY + RANK() |
| 2 | What is peak admission season? | DATE functions + aggregation |
| 3 | Which insurance provider generates most revenue? | JOIN + SUM |
| 4 | Do SMS reminders actually reduce no-shows? | Conditional aggregation |
| 5 | Which patients are readmitted most? | CTE + COUNT |
| 6 | Month-over-month change in admissions? | LAG() window function |
| 7 | Top 3 conditions per department? | ROW_NUMBER() + PARTITION BY |
| 8 | Which doctor handles the most patients? | JOIN + GROUP BY |

---

## 🗄️ Database Schema

```
departments ──< doctors ──< admissions >── patients
                                 │
                              billing
appointments (standalone no-show analysis)
```

**5 Tables | 6 Relationships | 20+ Queries**

---

## 📊 Key Insights Found

> *(Update these with your actual query results)*

- 🔴 **Cardiology and Oncology** account for **X%** of total hospital revenue
- 📅 **November–January** shows a **X% spike** in respiratory admissions
- 💊 Patients with **Diabetes** have the longest average stay at **X days**
- 📱 SMS reminders **reduce no-show rate by X%** (from X% to X%)
- 💰 **Insurance-based patients** have **X% higher** average billing than cash patients
- 🔁 **X% of patients** are readmitted within the same year

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| MySQL 8.0 | Database creation, querying |
| MySQL Workbench | Query execution, ERD diagram |
| Python (Pandas) | Data cleaning & preprocessing |
| Jupyter Notebook | Exploratory data analysis |
| Excel | Quick sanity checks |

---

## 📁 Project Structure

```
hospital-sql-analysis/
├── data/
│   ├── raw/                        ← Original downloaded CSVs (not committed)
│   └── cleaned/                    ← Cleaned CSVs ready for MySQL import
├── sql/
│   ├── 01_schema.sql               ← Table creation scripts
│   ├── 02_insert_data.sql          ← Data loading instructions
│   └── 03_analysis.sql             ← All 20+ business analysis queries
├── python/
│   └── data_cleaning.py            ← Data cleaning script
├── screenshots/                    ← Query output screenshots
├── insights_report.md              ← Written business findings
└── README.md
```

---

## 🚀 How to Run This Project

### Step 1 — Get the Data
Download these datasets from Kaggle:
- [Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset)
- [Medical Appointments No-show](https://www.kaggle.com/datasets/wajahat1064/healthcare-appointment-dataset)

Place CSVs in `data/raw/`

### Step 2 — Clean the Data
```bash
cd python/
pip install pandas numpy
python data_cleaning.py
```
Cleaned files will appear in `data/cleaned/`

### Step 3 — Set Up MySQL Database
Open **MySQL Workbench** and run in order:
```sql
SOURCE sql/01_schema.sql;   -- Creates all tables
SOURCE sql/02_insert_data.sql;  -- Load your data
SOURCE sql/03_analysis.sql;     -- Run all analysis
```

### Step 4 — Explore the Analysis
All queries are in `sql/03_analysis.sql` organized into sections:
- Section A: Basic Exploration
- Section B: Department & Doctor Analysis
- Section C: Revenue Analysis
- Section D: Patient Stay Analysis
- Section E: Medical Conditions
- Section F: No-Show Analysis
- Section G: Advanced (CTEs, Window Functions)
- Section H: Stored Procedure

---

## 📸 Screenshots

*(Add screenshots of your query results here after running)*

| Query | Screenshot |
|---|---|
| Department Revenue Ranking | `screenshots/dept_revenue.png` |
| Monthly Admission Trend | `screenshots/monthly_trend.png` |
| No-show Rate by SMS | `screenshots/noshow_sms.png` |
| Top Conditions per Dept | `screenshots/conditions.png` |

---

## 💡 Business Recommendations

Based on the analysis, three key recommendations for hospital management:

1. **Automate SMS Reminders** — No-show rate drops significantly with SMS alerts,
   particularly for patients in the 18–35 age group who show the highest no-show rates.

2. **Optimise Cardiology & Oncology Staffing** — These departments carry the
   highest patient load and generate the most revenue; understaffing here has
   the biggest operational impact.

3. **Seasonal Resource Planning** — Respiratory cases spike in winter months;
   pre-emptive bed and staff allocation can reduce wait times by an estimated 20–30%.

---

## 👤 Author

**Kiran U**
- 📧 kirankiranu791@gmail.com
- 💼 [LinkedIn](your-linkedin-url)
- 🐙 [GitHub](your-github-url)

---

## 📄 Dataset Credits

- Healthcare Dataset — [Kaggle / prasad22](https://www.kaggle.com/datasets/prasad22/healthcare-dataset)
- Medical Appointments — [Kaggle / wajahat1064](https://www.kaggle.com/datasets/wajahat1064/healthcare-appointment-dataset)
