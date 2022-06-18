SELECT
  Company.company_code,
  Company.founder,
  COUNT(
    DISTINCT Lead_Manager.lead_manager_code
  ),
  COUNT(
    DISTINCT Senior_Manager.senior_manager_code
  ),
  COUNT(DISTINCT Manager.manager_code),
  COUNT(DISTINCT Employee.employee_code)
FROM
  Company
  INNER JOIN Lead_Manager ON Company.company_code = Lead_Manager.company_code
  INNER JOIN Senior_Manager ON Company.company_code = Senior_Manager.company_code
  INNER JOIN Manager ON Company.company_code = Manager.company_code
  INNER JOIN Employee ON Company.company_code = Employee.company_code
GROUP BY
  Company.company_code,
  Company.founder
ORDER BY
  Company.company_code
