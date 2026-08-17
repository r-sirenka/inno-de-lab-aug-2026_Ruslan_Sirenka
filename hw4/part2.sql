CREATE TABLE Departments (
	DepartmentID SERIAL PRIMARY KEY,
	DepartmentName VARCHAR(50) UNIQUE NOT NULL,
	LOCATION VARCHAR(50)
);
ALTER TABLE employees 
	ADD COLUMN Email varchar(100);
UPDATE employees
SET email = LOWER(firstname || '.' || lastname || '@company.com');
ALTER TABLE employees 
	ADD CONSTRAINT UQ_Email UNIQUE (email);
ALTER TABLE departments 
	RENAME COLUMN location TO OfficeLocation;
