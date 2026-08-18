SELECT p.ProjectName
FROM Projects AS p
JOIN EmployeeProjects AS ep ON p.ProjectID = ep.ProjectID
JOIN Employees AS e ON ep.EmployeeID = e.EmployeeID
WHERE e.FirstName = 'Bob' 
  AND e.LastName = 'Johnson'
  AND ep.HoursWorked > 150;

UPDATE Projects
SET Budget = Budget * 1.10
WHERE ProjectID IN (
    SELECT DISTINCT ep.ProjectID
    FROM EmployeeProjects AS ep
    JOIN Employees AS e ON ep.EmployeeID = e.EmployeeID
    WHERE e.Department = 'IT'
); --никого нет в IT, в заданиях переводили в Senior IT

UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL; --в нашем случае ничего не поменялось, т.к. везде есть конечная дата

BEGIN;

WITH new_emp AS (
    INSERT INTO Employees (FirstName, LastName, Department, Salary)
    VALUES ('John', 'Ruber', 'IT', 50000.00)
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    EmployeeID,
    (SELECT ProjectID FROM Projects WHERE ProjectName = 'Website Redesign'),
    80
FROM new_emp;

COMMIT;