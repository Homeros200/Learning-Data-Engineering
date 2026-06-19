-- Detect if a cell is empty or contains one or more spaces.

WITH Orders AS (
SELECT 1 Id, 'A' Category UNION
SELECT 2, NULL UNION 
SELECT 3, ''    UNION
SELECT 4, '  ' 
)
SELECT
*,
 NULLIF(TRIM(Category), '') Policy2,
 COALESCE(NULLIF(TRIM(Category), ''), 'unknown') Policy3

FROM Orders
