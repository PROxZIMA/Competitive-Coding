SELECT
  round(ABS(MAX(LONG_W) - MIN(LAT_N)) + ABS(MAX(LAT_N) - MIN(LONG_W)), 4)
FROM
  STATION;