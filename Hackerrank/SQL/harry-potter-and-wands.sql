SELECT
  Wands.id,
  Wands_Property.age,
  Wands.coins_needed,
  Wands.POWER
FROM
  Wands
  JOIN Wands_Property ON Wands.code = Wands_Property.code
WHERE
  (
    Wands_Property.age, Wands.coins_needed,
    Wands.POWER
  ) IN (
    SELECT
      Wands_Property.age,
      MIN(Wands.coins_needed),
      Wands.POWER
    FROM
      Wands
      JOIN Wands_Property ON Wands.code = Wands_Property.code
    WHERE
      Wands_Property.is_evil = 0
    GROUP BY
      Wands_Property.age,
      Wands.POWER
  )
ORDER BY
  Wands.POWER DESC,
  Wands_Property.age DESC;
