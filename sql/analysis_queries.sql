create database hospital_analytics;

use hospital_analytics;
 
-- =============================================================
-- section 1: data verification
-- =============================================================
 
-- verify all tables loaded correctly
select 'patients'   as table_name, count(*) as total_rows from patients
union all
select 'admissions', count(*) from admissions
union all
select 'billing',    count(*) from billing;
 
-- =============================================================
-- section 2: medical condition analysis
-- =============================================================
 
-- which medical condition is most common?
-- business use: helps hospital allocate beds and staff per condition
select
    medical_condition,
    count(*) as total_cases,
    round(avg(length_of_stay), 1)   as avg_stay_days,
    round(avg(b.billing_amount), 2) as avg_billing
from admissions a
join billing b on a.patient_id = b.patient_id
group by medical_condition
order by total_cases desc;
 
-- =============================================================
-- section 3: revenue & insurance analysis
-- =============================================================
-- which insurance provider brings the most revenue?
-- business use: helps hospital prioritize insurance partnerships
select
    insurance_provider,
    count(*) as total_patients,
    round(sum(billing_amount), 2) as total_revenue,
    round(avg(billing_amount), 2) as avg_billing
from billing
group by insurance_provider
order by total_revenue desc;
 
 
-- =============================================================
-- section 4: yearly revenue trend
-- =============================================================
 
-- how is revenue growing year over year?
-- business use: annual performance tracking for management
select
    admission_year,
    count(*)                        as total_admissions,
    round(sum(b.billing_amount), 2) as total_revenue,
    round(avg(b.billing_amount), 2) as avg_per_patient
from admissions a
join billing b on a.patient_id = b.patient_id
group by admission_year
order by admission_year;
 
 
-- =============================================================
-- section 5: age group analysis
-- =============================================================
 
-- which age group has the most admissions and highest billing?
-- business use: helps design targeted healthcare packages
select
    age_group,
    count(*) as total_patients,
    round(avg(b.billing_amount), 2) as avg_billing
from patients p
join billing b on p.patient_id = b.patient_id
group by age_group
order by total_patients desc;
 
 
-- =============================================================
-- section 6: running total revenue (window function)
-- =============================================================
 
-- running total revenue month by month per year
-- business use: tracks cumulative revenue progress within each year
-- sql concept used: CTE + SUM() OVER() window function
with monthly as (
    select
        admission_year,
        admission_month,
        admission_month_name,
        round(sum(b.billing_amount), 2) as monthly_revenue
    from admissions a
    join billing b on a.patient_id = b.patient_id
    group by admission_year, admission_month, admission_month_name
)
select
    admission_year,
    admission_month_name,
    monthly_revenue,
    round(sum(monthly_revenue) over (
        partition by admission_year
        order by admission_month
    ), 2) as running_total_ytd
from monthly
order by admission_year, admission_month;
 
 
-- =============================================================
-- section 7: top doctors by patient volume
-- =============================================================
 
-- which doctors handle the most patients?
-- business use: identify top performers and workload distribution
select
    doctor_name,
    count(*)                        as patients_handled,
    round(avg(length_of_stay), 1)   as avg_stay_days,
    round(avg(b.billing_amount), 2) as avg_billing
from admissions a
join billing b on a.patient_id = b.patient_id
group by doctor_name
order by patients_handled desc
limit 10;
 
 
-- =============================================================
-- section 8: month over month change (window function)
-- =============================================================
 
-- how did admissions change month over month?
-- business use: spot sudden drops or spikes in patient volume
-- sql concept used: LAG() window function
with monthly_admissions as (
    select
        admission_year,
        admission_month,
        admission_month_name,
        count(*) as total_admissions
    from admissions
    group by admission_year, admission_month, admission_month_name
)
select
    admission_year,
    admission_month_name,
    total_admissions,
    lag(total_admissions) over (
        order by admission_year, admission_month
    ) as previous_month,
    total_admissions - lag(total_admissions) over (
        order by admission_year, admission_month
    ) as mom_change
from monthly_admissions
order by admission_year, admission_month;
 
 
-- =============================================================
-- section 9: admission type analysis
-- =============================================================
 
-- which admission type generates most revenue?
-- business use: helps understand emergency vs planned care revenue split
select
    admission_type,
    count(*)                        as total_cases,
    round(sum(b.billing_amount), 2) as total_revenue,
    round(avg(b.billing_amount), 2) as avg_billing,
    round(avg(length_of_stay), 1)   as avg_stay_days
from admissions a
join billing b on a.patient_id = b.patient_id
group by admission_type
order by total_revenue desc;
 
 
-- =============================================================
-- section 10: stored procedure
-- =============================================================
-- Create the procedure for every year report
DELIMITER $$
create procedure GetYearlyReport(in report_year int)
begin
    select
        admission_month_name as month,
        count(*) as admissions,
        round(sum(b.billing_amount), 2) as revenue,
        round(avg(length_of_stay), 1) as avg_stay
    from admissions a
    join billing b on a.patient_id = b.patient_id
    where admission_year = report_year
    group by admission_month, admission_month_name
    order by admission_month;
end$$
DELIMITER ;

-- Calling it
call GetYearlyReport(2024);
