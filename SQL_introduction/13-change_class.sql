-- Score too low
-- Script that removes all records with a score <= 5
SELECT score, name
FROM second_table
WHERE score > 5
ORDER BY score DESC;
