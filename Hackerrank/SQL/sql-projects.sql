SELECT
  MIN(Project.Start_Date) AS Start_Date,
  MAX(Project.End_Date)
FROM
  (
    SELECT
      Projects.Start_Date,
      Projects.End_Date,
      date_sub(
        Projects.Start_Date,
        INTERVAL ROW_NUMBER() OVER (
          ORDER BY
            Projects.Start_Date
        ) DAY
      ) AS Common
    FROM
      Projects
  ) AS Project
GROUP BY
  Project.Common
ORDER BY
  COUNT(*) ASC,
  Start_Date ASC;
