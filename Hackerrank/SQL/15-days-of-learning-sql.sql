SELECT
  S1.submission_date,
  (
    SELECT
      COUNT(DISTINCT S2.hacker_id)
    FROM
      Submissions AS S2
    WHERE
      S2.submission_date = S1.submission_date
      AND (
        SELECT
          COUNT(DISTINCT S3.submission_date)
        FROM
          Submissions S3
        WHERE
          S3.hacker_id = S2.hacker_id
          AND S3.submission_date < S1.submission_date
      ) = datediff(
        S1.submission_date, '2016-03-01'
      )
  ),
  (
    SELECT
      S2.hacker_id
    FROM
      Submissions AS S2
    WHERE
      S2.submission_date = S1.submission_date
    GROUP BY
      S2.hacker_id
    ORDER BY
      COUNT(S2.submission_id) DESC,
      S2.hacker_id
    LIMIT
      1
  ) AS id,
  (
    SELECT
      name
    FROM
      Hackers
    WHERE
      hacker_id = id
  )
FROM
  (
    SELECT
      DISTINCT submission_date
    FROM
      Submissions
  ) S1
GROUP BY
  S1.submission_date
ORDER BY
  S1.submission_date;
