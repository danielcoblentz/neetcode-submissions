-- Write your query below
-- if employee_id is odd and their name not stat with letter M, else bonus is zero


SELECT employee_id,
    CASE    
        WHEN employee_id % 2 != 0 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id

