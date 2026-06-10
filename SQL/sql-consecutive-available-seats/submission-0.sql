-- Write your query below
WITH cte AS (
    SELECT seat_id, free, 
        LEAD(free) OVER (ORDER BY seat_id) AS next_val,
        LAG(free) OVER (ORDER BY seat_id) AS prev_val
    FROM cinema
)
SELECT seat_id
FROM cte
WHERE free != 0 AND (
    (next_val IS NOT NULL AND next_val != 0) OR (prev_val IS NOT NULL AND prev_val != 0)
)
ORDER BY seat_id ASC;