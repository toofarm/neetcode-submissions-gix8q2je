-- Write your query below
WITH cte AS (
    SELECT log_id,
        CASE
            WHEN LAG(log_id) OVER (ORDER BY log_id ASC) IS NULL
                OR LAG(log_id) OVER (ORDER BY log_id ASC) < log_id - 1
            THEN 'true'
            ELSE 'false'
        END AS is_start_id,
        CASE
            WHEN LEAD(log_id) OVER (ORDER BY log_id ASC) IS NULL
                OR LEAD(log_id) OVER (ORDER BY log_id ASC) > log_id + 1
            THEN 'true'
            ELSE 'false'
        END AS is_end_id
    FROM logs
),
starts AS (
    SELECT log_id AS start_id,
        RANK() OVER (ORDER BY log_id ASC) AS num_rank 
    FROM cte
    WHERE is_start_id = 'true'
),
ends AS (
    SELECT log_id AS end_id,
        RANK() OVER (ORDER BY log_id ASC) AS num_rank 
    FROM cte
    WHERE is_end_id = 'true'
)
SELECT a.start_id, b.end_id
FROM starts a
LEFT JOIN ends b USING(num_rank)
ORDER BY start_id ASC;



