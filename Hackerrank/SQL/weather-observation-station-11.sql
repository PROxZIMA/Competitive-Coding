SELECT DISTINCT
(CITY)
FROM
  STATION
WHERE
  CITY regexp ".*[^aeiou]$"
  OR CITY regexp "^[^aeiou].*$";
