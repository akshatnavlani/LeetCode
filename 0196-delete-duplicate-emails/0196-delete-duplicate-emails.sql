# Write your MySQL query statement below
DELETE p FROM Person as p INNER JOIN Person as e ON p.email=e.email WHERE p.id>e.id