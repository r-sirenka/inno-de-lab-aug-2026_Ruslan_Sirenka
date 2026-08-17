UPDATE Employees SET salary = salary * 1.10
WHERE department = 'HR'

UPDATE Employees SET department = 'Senior IT'
WHERE salary > 70000.00

DELETE FROM Employees
WHERE EmployeeID NOT IN (SELECT EmployeeID FROM EmployeeProjects);

BEGIN;

INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('Big Data', 504000.00, '2026-08-03', '2026-08-31');

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES (1, 7, 211),
       (2, 7, 428);

COMMIT;