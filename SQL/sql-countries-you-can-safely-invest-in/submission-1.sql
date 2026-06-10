-- Write your query below
WITH cte AS (
    SELECT id, SPLIT_PART(phone_number, '-', 1) AS country_code
    FROM person
),
cte2 AS (
    SELECT a.country_code, ROUND(AVG(b.duration), 2) AS average_call
    FROM cte a
    LEFT JOIN calls b ON a.id = b.caller_id OR a.id = b.callee_id
    GROUP BY country_code
),
cte3 AS (
    SELECT country_code, average_call
    FROM cte2
    WHERE average_call > (
        SELECT AVG(duration)
        FROM calls
    )
)
SELECT b.name AS country
FROM cte3 a
LEFT JOIN country b USING(country_code);

