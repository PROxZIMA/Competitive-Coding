SELECT
  N,
  CASE
    WHEN
      P IS NULL OR P = ''
    THEN
      'Root'
    WHEN
      N IN
      (
        SELECT DISTINCT
          P
        FROM
          BST
      )
    THEN
      'Inner'
    ELSE
      'Leaf'
  END
FROM
  BST
ORDER BY
  N;
