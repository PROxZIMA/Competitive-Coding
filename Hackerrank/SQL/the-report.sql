SELECT
  IF(
    Grades.Grade < 8, 'NULL', Students.Name
  ),
  Grades.Grade,
  Students.Marks
FROM
  Students
  JOIN Grades
WHERE
  Students.Marks BETWEEN Grades.Min_Mark
  AND Grades.Max_Mark
ORDER BY
  Grades.Grade DESC,
  Students.Name ASC;
