-- Write your query below
WITH cte AS (
    SELECT ABS(x - LEAD(x) OVER(ORDER BY x ASC)) AS distance
    FROM point
    ORDER BY distance ASC
)
SELECT distance AS shortest
FROM cte
LIMIT 1;