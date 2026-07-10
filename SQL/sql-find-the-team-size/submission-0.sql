-- Write your query below
WITH cte AS (
    SELECT team_id, COUNT(*) AS team_size
    FROM employee
    GROUP BY team_id
)
SELECT a.employee_id, b.team_size
FROM employee a
LEFT JOIN cte b USING(team_id);