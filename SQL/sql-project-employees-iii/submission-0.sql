-- Write your query below
WITH cte AS (
    SELECT a.employee_id, a.name, a.experience_years, 
        b.project_id,
        DENSE_RANK() OVER (PARTITION BY b.project_id ORDER BY a.experience_years DESC) AS years_rank
    FROM employee a
    LEFT JOIN project b USING(employee_id)
)
SELECT project_id, employee_id
FROM cte
WHERE years_rank = 1;