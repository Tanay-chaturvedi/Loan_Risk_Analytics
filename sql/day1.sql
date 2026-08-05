create database loan_risk;
use loan_risk;
select count(*) from loan;
DESCRIBE loan;
select round(avg(income),2) as average from loan;
select max(income) as highest from loan;
select min(income) as highest from loan;
select sum(income) as highest from loan;
-- How many customers belong to each education level?
select education, count(*) as value from loan group by education;

-- What is the average income for each education level?
select education, round(avg(income),2) as average from loan group by education;

-- How many customers are there in each family size?
select family, count(*) as val from loan group by family;

-- How many customers have accepted a personal loan, and how many have not?
SELECT `Personal Loan`, COUNT(*) AS total_customers FROM loan GROUP BY `Personal Loan`;


-- Show family sizes ordered from the largest number of customers to the smallest.
select family, count(*) as val from loan group by family order by val desc;

select education, round(avg(mortgage),2) from loan group by education order by avg(mortgage) desc limit 1;
select family,round(avg(income),2) from loan group by family order by avg(income) desc limit 1;
select education, count(*) from loan  where `personal loan`=1 group by education order by count(*) desc limit 1;
