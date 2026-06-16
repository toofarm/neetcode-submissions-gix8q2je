-- Write your query below
WITH cte AS (
    SELECT COALESCE(a.employee_id, b.employee_id) AS employee_id, 
        a.name, b.salary
    FROM employees a
    FULL OUTER JOIN salaries b USING(employee_id)
)
SELECT employee_id
FROM cte
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id ASC;