-- Write your query below
WITH cte AS (
    SELECT a.name, a.account, COALESCE(SUM(b.amount), 0) AS balance
    FROM users a
    LEFT JOIN transactions b USING(account)
    GROUP BY name, account
)
SELECT name, balance
FROM cte
WHERE balance > 10000;