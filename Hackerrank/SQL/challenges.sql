SELECT
  Hackers.hacker_id,
  Hackers.name,
  COUNT(Challenges.challenge_id) AS Total
FROM
  Hackers
  JOIN Challenges ON Challenges.hacker_id = Hackers.hacker_id
GROUP BY
  Hackers.hacker_id,
  Hackers.name
HAVING
  Total = (
    SELECT
      MAX(Hacker.Cnt)
    FROM
      (
        SELECT
          COUNT(C.challenge_id) AS Cnt
        FROM
          Challenges AS C
        GROUP BY
          C.hacker_id
      ) AS Hacker
  )
  OR Total IN (
    SELECT
      Hacker.Cnt
    FROM
      (
        SELECT
          COUNT(C.challenge_id) AS Cnt
        FROM
          Challenges AS C
        GROUP BY
          C.hacker_id
      ) AS Hacker
    GROUP BY
      Hacker.Cnt
    HAVING
      COUNT(Hacker.Cnt) = 1
  )
ORDER BY
  Total DESC,
  Hackers.hacker_id ASC;
