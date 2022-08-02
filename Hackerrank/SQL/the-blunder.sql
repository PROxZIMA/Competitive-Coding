SELECT
  CEIL(AVG(Salary - replace(Salary, '0', '')))
FROM
  EMPLOYEES;
