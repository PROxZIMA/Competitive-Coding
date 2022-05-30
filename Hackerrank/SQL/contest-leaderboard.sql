SELECT
  Hacker.hacker_id,
  Hacker.name,
  SUM(Hacker.max_score) AS Total
FROM
  (
    SELECT
      Hackers.hacker_id,
      Hackers.name,
      MAX(Submissions.score) AS max_score
    FROM
      Hackers
      JOIN Submissions ON Submissions.hacker_id = Hackers.hacker_id
    GROUP BY
      Hackers.hacker_id,
      Hackers.name,
      Submissions.challenge_id
  ) AS Hacker
GROUP BY
  Hacker.hacker_id,
  Hacker.name
HAVING
  Total != 0
ORDER BY
  Total DESC,
  Hacker.hacker_id ASC;
