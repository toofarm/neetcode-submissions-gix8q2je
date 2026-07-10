-- Write your query below
WITH cte AS (
    SELECT DISTINCT a.account_id
    FROM log_info a
    JOIN log_info b ON a.account_id = b.account_id
        AND a.ip_address != b.ip_address
        AND b.login BETWEEN a.login AND a.logout
),
cte2 AS (
    SELECT DISTINCT a.account_id
    FROM log_info a
    JOIN log_info b ON a.account_id = b.account_id
        AND a.ip_address != b.ip_address
        AND b.logout BETWEEN a.login AND a.logout
)
SELECT DISTINCT account_id FROM cte
UNION
SELECT DISTINCT account_id FROM cte2;

-- SELECT DISTINCT a.account_id
-- FROM log_info a
-- INNER JOIN log_info b ON a.account_id = b.account_id
--     AND a.ip_address != b.ip_address
--     AND b.login BETWEEN a.login AND a.logout
--     OR b.logout BETWEEN a.login AND a.logout;