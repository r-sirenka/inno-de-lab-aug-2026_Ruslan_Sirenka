UPDATE Employees SET salary = salary * 1.10
WHERE department = 'HR'

UPDATE Employees SET department = 'Senior IT'
WHERE salary > 70000.00
LIMIT 1; -- можно просто взять EmploeesID = 2, но думаю так правильнее, если бы база была оч большой

DELETE FROM Employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM EmployeeProjects ep
    WHERE ep.EmployeeID = e.EmployeeID
);

BEGIN;

INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('Big Data', 504000.00, '2026-08-03', '2026-08-31');

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES 
    (1, currval('projects_projectid_seq'), 211),
    (2, currval('projects_projectid_seq'), 428);

COMMIT;