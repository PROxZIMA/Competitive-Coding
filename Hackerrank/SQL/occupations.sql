SELECT
  MIN(IF(O.Occupation = 'Doctor', O.Name, NULL)),
  MIN(IF(O.Occupation = 'Professor', O.Name, NULL)),
  MIN(IF(O.Occupation = 'Singer', O.Name, NULL)),
  MIN(IF(O.Occupation = 'Actor', O.Name, NULL))
FROM
  (
    SELECT
      MAX(O1.Occupation) AS Occupation,
      O1.Name AS Name,
      COUNT(O2.Name) - 1 AS `RANK`
    FROM
      OCCUPATIONS O1
      JOIN OCCUPATIONS O2 ON O1.Occupation = O2.Occupation
    WHERE
      O1.Name >= O2.Name
    GROUP BY
      O1.Name
  ) AS O
GROUP BY
  O.RANK
ORDER BY
  O.RANK;
