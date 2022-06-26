SET
  @median = (
    SELECT
      FLOOR(
        COUNT(LAT_N) / 2
      )
    FROM
      STATION
  );
SET
  @stmt = CONCAT(
    'SELECT round(LAT_N, 4) FROM STATION ORDER BY LAT_N LIMIT ',
    @median, ', ', 1
  );
PREPARE cmd
FROM
  @stmt;
EXECUTE cmd;
DEALLOCATE PREPARE cmd;
