use loan_risk;
select id,income, row_number() over(order by income desc) as rn from loan;

select id,CCAvg,rank() over(order by CCAvg desc) as Ra from loan;

-- Display the Top 5 highest-income customers using ROW_NUMBER().
-- (Hint: A subquery or CTE will help.)

select id,income,inc,education from ( select id,income,education, row_number() over (partition by education order by income desc) as inc from loan) as ranikng where inc <=5;

select id, row_number() over(order by income desc) as ranking from loan;

select id,CCAvg,ranking from ( select id,CCAvg,row_number() over(order by CCAvg desc) as ranking from loan) as Result where ranking <=3;

select id,income,ranking,education from( select id,income,education,row_number() over(partition by education order by income desc) as ranking from loan) as result where ranking =1;
select id,income,ranking,education from( select id,income,education,row_number() over(partition by education order by income desc) as ranking from loan) as result where ranking <=2;
select id,family,mortgage,ranking from ( select id,family,mortgage,dense_rank() over(partition by family order by mortgage desc) as ranking from loan) as result;
select id,income,education,ranking from ( select id,income,education , dense_rank() over (partition by education order by income desc)as ranking from loan) as result where ranking =2;