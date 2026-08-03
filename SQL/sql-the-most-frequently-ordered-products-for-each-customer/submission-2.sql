-- Write your query below
WITH cte AS (
    SELECT customer_id, product_id, COUNT(*) AS num_ordered
    FROM orders
    GROUP BY customer_id, product_id
),
cte2 AS (
    SELECT a.customer_id, a.product_id, b.product_name,
        RANK() OVER (PARTITION BY customer_id ORDER BY num_ordered DESC) AS order_rank
    FROM cte a
    LEFT JOIN products b USING(product_id)
)
SELECT a.customer_id, b.product_id, b.product_name
FROM customers a
LEFT JOIN cte2 b ON a.customer_id = b.customer_id
WHERE b.order_rank = 1;