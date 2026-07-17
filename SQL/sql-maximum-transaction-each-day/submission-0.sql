-- Write your query below
WITH cte AS (
    SELECT *, CAST(day AS date) AS date_only
    FROM transactions
),
cte2 AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY date_only ORDER BY amount DESC) AS date_rank
    FROM cte
)
SELECT transaction_id
FROM cte2
WHERE date_rank = 1
ORDER BY transaction_id ASC;