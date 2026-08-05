CREATE TABLE branch (
    ID INT PRIMARY KEY,
    Branch_Name VARCHAR(30),
    Branch_City VARCHAR(30)
);
INSERT INTO branch VALUES
(1,'Bangalore','Bangalore'),
(2,'Mumbai','Mumbai'),
(3,'Delhi','Delhi'),
(4,'Chennai','Chennai'),
(5,'Hyderabad','Hyderabad'),
(6,'Pune','Pune'),
(7,'Kolkata','Kolkata'),
(8,'Ahmedabad','Ahmedabad'),
(9,'Jaipur','Jaipur'),
(10,'Lucknow','Lucknow');
select * from branch;
-- The bank wants to know the branch assigned to customers.
select l.id,l.age,l.income,b.branch_name from loan l inner join branch b on l.id=b.id;

select l.id,l.age,l.income,b.branch_name from loan l left join branch b on l.id=b.id;

select l.id,l.age,l.income,b.branch_name from branch b left join loan l on l.id=b.id;

select l.id,l.age,l.income,b.branch_name from loan l inner join branch b on l.id=b.id where b.Branch_City="Bangalore";

select b.branch_city,count(*) from loan l inner join branch b on l.id=b.id group by b.Branch_city;

select id,income from loan where income > (select avg(income) from loan) ;
select id from loan where mortgage = (select max(Mortgage) from loan);


-- 2nd max income
select * from loan where income=(
select max(income) from loan where income < 
(select max(income) from loan));


-- CTE (Common Table Expression)
-- Create a CTE named HighIncome that stores customers with income greater than 100, then display all records from it.
with HighIncome as(
	select id from loan where income > 100
)
select * from HighIncome;

with LoanAccepted as (
	select id,income from loan where `Personal Loan`=1
)
select *  from LoanAccepted;
