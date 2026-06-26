USE SalesDB
-- Segment all orders into 3 categories: high, medium and low sales.
SELECT
*,
CASE WHEN Buckets = 1 THEN 'High'
     WHEN Buckets = 2 THEN 'MEDIUM'
     WHEN Buckets = 3 THEN 'LOW'
END SalesSegmentations

FROM (
SELECT
OrderID,
Sales,
NTILE(3) OVER (ORDER BY Sales DESC) Buckets
FROM Sales.Orders
)t




