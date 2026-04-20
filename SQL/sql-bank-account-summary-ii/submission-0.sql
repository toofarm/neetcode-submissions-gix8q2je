-- Write your query below
WITH cte AS (
    SELECT a.name, SUM(b.amount) AS balance
    FROM users a
    LEFT JOIN transactions b USING(account)
    GROUP BY name
)
SELECT name, balance
FROM cte
WHERE balance > 10000;