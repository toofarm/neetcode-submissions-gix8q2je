-- Write your query below
SELECT name
FROM sales_person
WHERE sales_id NOT IN (
    SELECT a.sales_id
    FROM orders a
    LEFT JOIN company b USING(com_id)
    WHERE b.name = 'CRIMSON'
);