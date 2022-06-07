SELECT
  Students.Name
FROM
  Students
  JOIN Friends     ON Friends.ID = Students.ID
  JOIN Packages P1 ON P1.ID = Students.ID
  JOIN Packages P2 ON P2.ID = Friends.Friend_ID
WHERE
  P2.Salary > P1.Salary
ORDER BY
  P2.Salary;
