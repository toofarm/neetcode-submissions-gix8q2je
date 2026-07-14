-- Write your query below
WITH cte AS (
    SELECT *,
        RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS login_num
    FROM activity
) 
SELECT player_id, device_id
FROM cte
WHERE login_num = 1;
