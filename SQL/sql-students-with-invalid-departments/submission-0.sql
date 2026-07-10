-- Write your query below
WITH cte AS (
    SELECT a.id, a.name, b.name AS department_name
    FROM students a
    LEFT JOIN departments b ON a.department_id = b.id
)
SELECT id, name
FROM cte
WHERE department_name IS NULL;