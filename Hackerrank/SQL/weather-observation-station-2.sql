SELECT
  round(SUM(LAT_N), 2),
  round(SUM(LONG_W), 2)
FROM
  STATION;
