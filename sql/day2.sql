use loan_risk;
select id from loan where income>100 and `personal loan`=1;
select * from loan where `personal loan`=1;
select * from loan where family=4;

-- Show only those education levels where the average income is greater than 70.
select education, avg(income) as average from loan group by education having average >70;

-- CASE
--     WHEN condition THEN value
--     WHEN condition THEN value
--     ELSE value
-- END



-- Create an Income Category:
select income,case
	when income < 50 then "low"
    when income < 100 then "mid"
    else "high"
end as Category from loan;

-- Count how many customers belong to each Income Category.
select case
	when income < 50 then "low"
    when income < 100 then "mid"
    else "high"
end as Category, count(*) from loan group by Category;

-- Find the average credit card spending (CCAvg) for each Income Category.
select case
	when income < 50 then "low"
    when income < 100 then "mid"
    else "high"
end as Category, round(avg(CCAvg),2) from loan group by Category;

