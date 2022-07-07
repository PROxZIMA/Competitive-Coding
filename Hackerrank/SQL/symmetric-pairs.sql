SELECT
  DISTINCT F1.X,
  F1.Y
FROM
  (
    SELECT
      Functions.X,
      Functions.Y,
      ROW_NUMBER() OVER (
        ORDER BY
          Functions.X
      ) AS RN
    FROM
      Functions
  ) F1
  JOIN (
    SELECT
      Functions.X,
      Functions.Y,
      ROW_NUMBER() OVER (
        ORDER BY
          Functions.X
      ) AS RN
    FROM
      Functions
  ) F2 ON F1.X = F2.Y
  AND F1.Y = F2.X
  AND F1.RN != F2.RN
WHERE
  F1.X <= F1.Y
ORDER BY
  F1.X;
