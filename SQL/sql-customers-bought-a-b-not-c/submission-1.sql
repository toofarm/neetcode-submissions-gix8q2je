-- Write your query below
WITH cte AS (
    SELECT a.customer_id, a.customer_name, b.product_name
    FROM customers a
    LEFT JOIN orders b USING(customer_id)
    GROUP BY customer_id, product_name
)
SELECT customer_id, customer_name
FROM cte
GROUP BY customer_id, customer_name
HAVING SUM(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) < 1
ORDER BY customer_name;