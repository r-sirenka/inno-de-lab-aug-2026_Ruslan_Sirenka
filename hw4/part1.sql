INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES 
	('Andrey', 'Sirenka', 'HR', 100500.00),
	('Kristina', 'Popova', 'BigData', 6900.00);
SELECT *
FROM Employees;
SELECT firstname, lastname
FROM Employees
WHERE department = 'IT';
UPDATE Employees
SET
	salary = 65000.00
WHERE EmployeeID = 1;
DELETE
FROM Employees
WHERE EmployeeID = 5;
SELECT *
FROM Employees;
