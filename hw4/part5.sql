CREATE OR REPLACE FUNCTION CalculateAnnualBonus(employee_id INT, Salary NUMERIC)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN Salary * 0.10;
END;
$$;

SELECT 
    EmployeeID, 
    FirstName, 
    LastName, 
    Salary, 
    CalculateAnnualBonus(EmployeeID, Salary) AS Bonus
FROM Employees;

CREATE VIEW IT_Department_View AS
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Department = 'IT';

SELECT * FROM IT_Department_View; --сотрудников нет, т.к. всех перевели в прошлом задании
