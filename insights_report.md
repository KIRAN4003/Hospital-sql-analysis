# 📋 Hospital Analytics — Insights Report

**Author:** Kiran U  
**Project:** Hospital Operations & Patient Analytics  
**Tools:** MySQL, Python (Pandas)

---

## Executive Summary

This analysis examines hospital operations across patient admissions, revenue,
department performance, and appointment behaviour. Using SQL on a structured
relational database, we identified key inefficiencies and revenue drivers that
can directly inform management decisions.

---

## Finding 1 — Department Load & Revenue

**Query used:** Section B1, C1 in analysis.sql

**What we found:**
*(Fill in after running queries — example format below)*

> Cardiology and Oncology together account for **XX%** of total hospital revenue,
> yet represent only **XX%** of total departments. Cardiology shows the highest
> admissions-per-bed ratio at **X.X**, indicating near-capacity utilisation.

**Business recommendation:**
Prioritise staffing and bed expansion in Cardiology. A 10% increase in Cardiology
capacity could yield an estimated **₹X lakhs** in additional annual revenue.

---

## Finding 2 — Seasonal Admission Patterns

**Query used:** Section C4 in analysis.sql

**What we found:**
> Hospital admissions peak in **[Month]** and **[Month]**, with a **XX%** spike
> compared to the annual average. Respiratory conditions show the strongest
> seasonality, rising **XX%** in winter months (Nov–Jan).

**Business recommendation:**
Pre-position respiratory care staff and equipment in October. Consider partnering
with local pharmacies for preventive care campaigns before the winter peak.

---

## Finding 3 — Appointment No-Show Analysis

**Query used:** Section F1–F5 in analysis.sql

**What we found:**
> The overall no-show rate is **XX%**. Patients who received SMS reminders showed
> a no-show rate of **XX%** versus **XX%** for those who did not — a reduction
> of **XX percentage points**.
>
> The **18–35 age group** had the highest no-show rate at **XX%**.  
> Appointments scheduled **30+ days in advance** had **XX%** higher no-show rates
> than same-day or next-week bookings.

**Business recommendation:**
Implement mandatory SMS + WhatsApp reminders 48 hours before every appointment.
Based on current no-show volume, this could recover approximately **₹X lakhs**
in lost appointment revenue annually.

---

## Finding 4 — Most Costly Medical Conditions

**Query used:** Section E2 in analysis.sql

**What we found:**
> **[Condition Name]** has the highest average billing at ₹**XX,XXX** per patient,
> followed by **[Condition 2]** at ₹**XX,XXX**.  
> Patients with **[Condition]** also have the longest average stay at **X days**,
> compounding both clinical and financial burden.

**Business recommendation:**
Negotiate targeted insurance packages for high-cost conditions. Consider a
dedicated case management programme for patients with these conditions to
reduce unnecessary length of stay.

---

## Finding 5 — Readmission Patterns

**Query used:** Section G3 in analysis.sql

**What we found:**
> **XX%** of patients were admitted more than once within the dataset period.
> Readmitted patients generate **XX%** higher average billing and account for a
> disproportionate share of long-stay cases.

**Business recommendation:**
Introduce a post-discharge follow-up protocol (phone call at day 7 and day 30)
for high-risk conditions. Evidence suggests this can reduce 30-day readmission
rates by 15–25%.

---

## SQL Techniques Used

| Technique | Where Used |
|---|---|
| JOINs (INNER, LEFT) | Almost every query |
| GROUP BY + Aggregations | Sections B, C, D, E |
| Subqueries | Section E |
| CTEs (WITH clause) | Section G1, G2, G3 |
| Window Functions (RANK, ROW_NUMBER, LAG) | Section G |
| CASE statements | Section F5 |
| Stored Procedures | Section H |
| Date Functions (MONTHNAME, DATEDIFF) | Sections C, F |

---

*Fill in all [XX] placeholders with actual numbers after running the queries.*
*Take screenshots of each key query result and add to /screenshots folder.*
