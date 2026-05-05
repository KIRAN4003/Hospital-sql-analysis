# 📋 Hospital Analytics — Insights Report

**Author:** Kiran U
**Project:** Hospital Operations & Patient Analytics
**Tools:** MySQL 8.0, Python (Pandas), SQLAlchemy
**Dataset:** 55,500 patient records — Healthcare Dataset (Kaggle)

---

## Executive Summary

This analysis examines hospital operations across patient admissions, medical
conditions, revenue, insurance providers, and doctor performance. Using advanced
SQL on a 3-table relational database, we identified key revenue drivers and
operational patterns that can directly inform hospital management decisions.

---

## Finding 1 — Medical Condition Analysis

**Query used:** Section 2 in analysis_queries.sql

**What we found:**

| Medical Condition | Total Cases | Avg Stay (Days) | Avg Billing ($) |
|---|---|---|---|
| Arthritis | 9,308 | 15.5 | 25,497 |
| Diabetes | 9,304 | 15.4 | 25,638 |
| Hypertension | 9,245 | 15.5 | 25,497 |
| Obesity | 9,231 | 15.5 | 25,805 |
| Cancer | 9,227 | 15.5 | 25,161 |
| Asthma | 9,185 | 15.7 | 25,635 |

**Key insight:**
Arthritis is the most prevalent condition at 9,308 cases. All 6 conditions
show near-equal distribution (~9,200 cases each), suggesting the hospital
serves a balanced patient mix rather than specialising in any single condition.
Average billing is consistent at ~$25,500 across all conditions.

**Business recommendation:**
Since no single condition dominates, the hospital should invest equally in
all 6 departments rather than over-specialising. Preventive care programmes
targeting Diabetes and Hypertension (lifestyle conditions) could reduce
long-term admission volume and improve patient outcomes.

---

## Finding 2 — Insurance Provider Revenue Analysis

**Query used:** Section 3 in analysis_queries.sql

**What we found:**

| Insurance Provider | Total Patients | Total Revenue | Avg Billing |
|---|---|---|---|
| Cigna | 11,249 | $287,139,345 | $25,525 |
| Medicare | 11,154 | $285,720,757 | $25,615 |
| Blue Cross | 11,059 | $283,254,294 | $25,613 |
| UnitedHealthcare | 11,125 | $282,454,542 | $25,389 |
| Aetna | 10,913 | $278,863,102 | $25,553 |

**Key insight:**
Cigna is the top revenue-generating insurance provider at $287M across 11,249
patients. All 5 providers show near-equal average billing at ~$25,500, meaning
revenue differences are driven by patient volume not billing rates.
Combined total revenue across all providers exceeds **$1.4 Billion.**

**Business recommendation:**
Cigna and Medicare together contribute over $572M — more than 40% of total
revenue. Strengthening these two partnerships through dedicated service
agreements and priority scheduling could significantly protect revenue stability.

---

## Finding 3 — Yearly Revenue Trend

**Query used:** Section 4 in analysis_queries.sql

**What we found:**
Revenue data spans multiple years with 2024 being the most recent year.
April 2024 was the peak admission month with **946 admissions** generating
**$23.5M** in revenue and an average stay of **16.2 days** — the highest
of any month in the dataset.

**Business recommendation:**
Pre-position additional staff and bed capacity before April each year.
Based on the April spike pattern, hiring contract staff for March–May
could prevent capacity bottlenecks during peak periods.

---

## Finding 4 — Age Group Analysis

**Query used:** Section 5 in analysis_queries.sql

**What we found:**
Patient admissions are distributed across all age groups. The analysis
reveals which age segments generate the most admissions and highest
average billing — helping the hospital design targeted healthcare packages
for high-value patient segments.

**Business recommendation:**
Develop age-specific health packages — particularly for the 51–65 and
65+ age groups who typically have higher billing amounts due to more
complex conditions and longer stays.

---

## Finding 5 — Month Over Month Revenue (Running Total)

**Query used:** Section 6 in analysis_queries.sql — CTE + Window Function

**What we found:**
Using a CTE combined with the `SUM() OVER()` window function, we tracked
cumulative revenue growth within each year. This allows management to
compare year-to-date performance at any point in the year against
the same period in previous years.

**SQL concept used:**
```sql
sum(monthly_revenue) over (
    partition by admission_year
    order by admission_month
) as running_total_ytd
```

**Business recommendation:**
Set monthly revenue targets based on the running total pattern. If cumulative
revenue by Month 4 (April) falls below the historical average, it signals
early intervention is needed to boost admissions or billing recovery.

---

## Finding 6 — Top Doctors by Patient Volume

**Query used:** Section 7 in analysis_queries.sql

**What we found:**
Top 10 doctors each handle a similar number of patients, indicating
balanced workload distribution across the medical staff. Average stay
days and billing are consistent across doctors at ~15.5 days and ~$25,500.

**Business recommendation:**
The balanced distribution is a positive sign. However, tracking this
monthly via the stored procedure can quickly flag if any doctor's
patient load spikes — an early warning for burnout or understaffing.

---

## Finding 7 — Stored Procedure for Automated Reporting

**Query used:** Section 9 in analysis_queries.sql

**What we found:**
A reusable stored procedure `GetYearlyReport()` was built that generates
a complete monthly breakdown of admissions, revenue, and average stay
for any given year with a single command:

```sql
CALL GetYearlyReport(2024);
CALL GetYearlyReport(2023);
```

**Business value:**
Instead of writing the full query every month, the hospital reporting
team can call this procedure in seconds — saving time and ensuring
consistent reporting methodology across all years.

---

## SQL Techniques Used

| Technique | Query Section | Purpose |
|---|---|---|
| INNER JOIN | All sections | Combine patients, admissions, billing |
| GROUP BY + Aggregations | Sections 2–5, 7–8 | Summarise data by category |
| ORDER BY | All sections | Sort results meaningfully |
| ROUND() | All sections | Clean decimal presentation |
| CTE (WITH clause) | Sections 6, 8 | Create reusable temp results |
| SUM() OVER() | Section 6 | Running total window function |
| LAG() | Section 8 | Month over month comparison |
| PARTITION BY | Section 6 | Reset running total per year |
| Stored Procedure | Section 9 | Reusable automated report |
| LIMIT | Section 7 | Top N results |

---

## Overall Business Impact

This SQL analysis on 55,500 hospital records delivered the following
actionable findings for hospital management:

1. **Revenue** — Identified Cigna as top partner ($287M) and April as
   peak revenue month ($23.5M) for better financial planning
2. **Conditions** — Equal distribution across 6 conditions supports
   balanced resource allocation strategy
3. **Automation** — Stored procedure enables monthly reporting in
   seconds without manual query writing
4. **Staffing** — Balanced doctor workload confirmed; monitoring system
   now in place via stored procedure

---

*Project completed by Kiran U — Aspiring Data Analyst*
*Contact: kirankiranu791@gmail.com*
*GitHub: https://github.com/KIRAN4003
