-- Count 89
-- Display the number of records
SELECT id, COUNT(*) AS count
FROM first_table
GROUP BY id;
