-- Write your query below
WITH cte AS (
    SELECT order_date, product_id, order_id,
        RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS order_rank
    FROM orders
)
SELECT b.product_name, a.product_id, a.order_id, a.order_date
FROM cte a
LEFT JOIN products b USING(product_id)
WHERE a.order_rank = 1
ORDER BY product_name ASC, product_id ASC, order_id ASC;