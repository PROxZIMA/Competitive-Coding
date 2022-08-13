SELECT
  Hackers.hacker_id,
  Hackers.name
FROM
  Hackers
  JOIN Submissions ON Submissions.hacker_id = Hackers.hacker_id
  JOIN Challenges  ON Challenges.challenge_id = Submissions.challenge_id
  JOIN Difficulty  ON Difficulty.difficulty_level = Challenges.difficulty_level
WHERE
  Submissions.score = Difficulty.score
GROUP BY
  Hackers.hacker_id,
  Hackers.name
HAVING
  COUNT(Submissions.hacker_id) > 1
ORDER BY
  COUNT(Submissions.hacker_id) DESC,
  Hackers.hacker_id ASC;
