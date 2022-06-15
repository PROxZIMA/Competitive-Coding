SELECT
  Contests.contest_id,
  Contests.hacker_id,
  Contests.name,
  SUM(SS.total_submissions) AS total_submissions,
  SUM(SS.total_accepted_submissions) AS total_accepted_submissions,
  SUM(VS.total_views) AS total_views,
  SUM(VS.total_unique_views) AS total_unique_views
FROM
  Contests
  JOIN Colleges ON Colleges.contest_id = Contests.contest_id
  JOIN Challenges ON Challenges.college_id = Colleges.college_id
  LEFT JOIN (
    SELECT
      challenge_id,
      SUM(total_views) AS total_views,
      SUM(total_unique_views) AS total_unique_views
    FROM
      View_Stats
    GROUP BY
      View_Stats.challenge_id
  ) AS VS ON VS.challenge_id = Challenges.challenge_id
  LEFT JOIN (
    SELECT
      challenge_id,
      SUM(total_submissions) AS total_submissions,
      SUM(total_accepted_submissions) AS total_accepted_submissions
    FROM
      Submission_Stats
    GROUP BY
      Submission_Stats.challenge_id
  ) AS SS ON SS.challenge_id = Challenges.challenge_id
GROUP BY
  Contests.contest_id,
  Contests.hacker_id,
  Contests.name
HAVING
  total_submissions + total_accepted_submissions + total_views + total_unique_views != 0
ORDER BY
  Contests.contest_id;
