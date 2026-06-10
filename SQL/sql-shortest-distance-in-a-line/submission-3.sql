-- Write your query below
SELECT ABS(x - LEAD(x) OVER(ORDER BY x ASC)) AS shortest
FROM point
ORDER BY shortest ASC
LIMIT 1;