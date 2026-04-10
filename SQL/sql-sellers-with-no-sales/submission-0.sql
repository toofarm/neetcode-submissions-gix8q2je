-- Write your query below
WITH cte AS (
    SELECT seller_id
    FROM orders
    WHERE sale_date > '2019-12-31' AND sale_date < '2021-01-01'
)
SELECT seller_name
FROM seller 
WHERE seller_id NOT IN (
    SELECT seller_id
    FROM cte
)
ORDER BY seller_name ASC;