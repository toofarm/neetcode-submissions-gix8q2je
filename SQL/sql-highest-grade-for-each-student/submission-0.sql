-- Write your query below
WITH cte AS (
    SELECT student_id, MAX(score) AS score
    FROM exam_results
    GROUP BY student_id
)
SELECT a.student_id, MIN(b.exam_id) AS exam_id, a.score
FROM cte a
LEFT JOIN exam_results b
    ON a.student_id = b.student_id AND a.score = b.score
GROUP BY a.student_id, a.score
ORDER BY student_id ASC;