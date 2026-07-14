-- Write your query below
WITH cte AS (
    SELECT name, salary, department_id,
        RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
    FROM employee
)
SELECT b.name AS department, a.name AS employee, a.salary
FROM cte a
LEFT JOIN department b ON a.department_id = b.id
WHERE salary_rank = 1 AND b.name IS NOT NULL;