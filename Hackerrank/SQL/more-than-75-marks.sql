SELECT
  Name
FROM
  STUDENTS
WHERE
  Marks > 75
ORDER BY
  substr(Name, - 3) ASC,
  ID ASC;
