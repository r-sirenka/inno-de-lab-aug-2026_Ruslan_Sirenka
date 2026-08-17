CREATE USER hr_user WITH PASSWORD '123pass';

CREATE ROLE selector;
GRANT SELECT ON Employees TO selector;

GRANT selector TO hr_user;

GRANT INSERT, UPDATE ON Employees TO hr_user;