SELECT DISTINCT
(CITY)
FROM
  STATION
WHERE
  CITY regexp "^[^aeiou].*[^aeiou]$";
