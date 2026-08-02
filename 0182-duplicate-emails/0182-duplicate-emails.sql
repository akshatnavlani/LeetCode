# Write your MySQL query statement below
SELECT p.email FROM Person as P GROUP BY p.email HAVING count(*)>1