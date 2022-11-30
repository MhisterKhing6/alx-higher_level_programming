-- list the number of records having the same scores
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;