-- Cheating is bad
-- Script that updates the score of Bob to 10
SELECT score, name 
FROM second_table
ORDER BY score DESC;

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
