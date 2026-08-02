# Write your MySQL query statement below
SELECT e.name as Employee FROM Employee as e WHERE (SELECT salary FROM Employee WHERE id = e.managerId)<e.salary