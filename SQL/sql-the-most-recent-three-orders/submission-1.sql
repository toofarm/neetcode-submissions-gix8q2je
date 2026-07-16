-- Write your query below
WITH cte AS (
    SELECT order_id, order_date, customer_id,
        DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS date_rank
    FROM orders
)
SELECT b.name AS customer_name, a.customer_id, a.order_id, a.order_date
FROM cte a
LEFT JOIN customers b USING(customer_id)
WHERE a.date_rank < 4 AND b.name IS NOT NULL
ORDER BY b.name ASC, a.customer_id ASC, a.order_date DESC;