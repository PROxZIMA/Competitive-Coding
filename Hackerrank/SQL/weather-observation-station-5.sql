SELECT
  CITY,
  length(CITY)
FROM
  STATION
ORDER BY
  length(CITY),
  CITY ASC LIMIT 1;
SELECT
  CITY,
  length(CITY)
FROM
  STATION
ORDER BY
  length(CITY) DESC,
  CITY ASC LIMIT 1;