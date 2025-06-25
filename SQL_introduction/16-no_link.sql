-- script that lists all records of a table of a datbase
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;