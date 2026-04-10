-- Write your query below
-- WITH left_side AS (
--     SELECT a.left_operand, b.value AS left_operand_value
--     FROM expressions a
--     LEFT JOIN variables b ON a.left_operand = b.name
-- ),
-- right_side AS (
--     SELECT a.right_operand, b.value AS right_operand_value
--     FROM expressions a
--     LEFT JOIN variables b ON a.right_operand = b.name
-- )
SELECT a.left_operand, a.operator, a.right_operand,
    CASE
        WHEN a.operator = '>' THEN b.value > c.value
        WHEN a.operator = '<' THEN b.value < c.value
        WHEN a.operator = '=' THEN b.value = c.value
    END AS value
FROM expressions a
LEFT JOIN variables b ON a.left_operand = b.name
LEFT JOIN variables c ON a.right_operand = c.name;
