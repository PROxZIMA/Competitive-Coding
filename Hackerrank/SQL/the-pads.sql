SELECT
  concat(Name, '(', substr(Occupation, 1, 1), ')')
FROM
  OCCUPATIONS
ORDER BY
  Name;
SELECT
  concat('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.') AS c
FROM
  OCCUPATIONS
GROUP BY
  Occupation
ORDER BY
  c ASC,
  Occupation ASC;
