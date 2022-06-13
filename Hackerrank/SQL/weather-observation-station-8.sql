-- SELECT DISTINCT
-- (CITY)
-- FROM
--   STATION
-- WHERE
--   (
--     CITY LIKE "%a"
--     OR CITY LIKE "%e"
--     OR CITY LIKE "%i"
--     OR CITY LIKE "%o"
--     OR CITY LIKE "%u"
--   )
--   AND
--   (
--     CITY LIKE "a%"
--     OR CITY LIKE "e%"
--     OR CITY LIKE "i%"
--     OR CITY LIKE "o%"
--     OR CITY LIKE "u%"
--   )
-- ;
-- SELECT DISTINCT
-- (CITY)
-- FROM
--   STATION
-- WHERE
--   LOWER(substr(CITY, - 1)) IN
--   (
--     'a',
--     'e',
--     'i',
--     'o',
--     'u'
--   )
--   AND LOWER(substr(CITY, 1, 1)) IN
--   (
--     'a',
--     'e',
--     'i',
--     'o',
--     'u'
--   )
-- ;
SELECT DISTINCT
(CITY)
FROM
  STATION
WHERE
  CITY regexp "^[aeiou].*[aeiou]$";
