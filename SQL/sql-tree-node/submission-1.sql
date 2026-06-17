-- Write your query below
WITH root AS (
    SELECT id, 'Root' AS type
    FROM tree
    WHERE p_id IS NULL
),
leaves AS (
    SELECT id, 'Leaf' AS type
    FROM tree
    WHERE id NOT IN (
        SELECT a.id
        FROM tree a
        INNER JOIN tree b ON a.id = b.p_id
    ) AND p_id IS NOT NULL
),
inners AS (
    SELECT id, 'Inner' AS type
    FROM tree
    WHERE id IN (
        SELECT a.id
        FROM tree a
        INNER JOIN tree b ON a.id = b.p_id
    ) AND p_id IS NOT NULL
)
SELECT id, type
FROM root
UNION
SELECT id, type
FROM leaves
UNION
SELECT id, type
FROM inners;
