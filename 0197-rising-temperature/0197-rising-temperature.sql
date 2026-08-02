# Write your MySQL query statement below
SELECT w.id FROM Weather w,Weather p WHERE w.temperature >p.temperature and w.recordDate = DATE_ADD(p.recordDate, INTERVAL 1 DAY) ORDER BY w.recordDate DESC
