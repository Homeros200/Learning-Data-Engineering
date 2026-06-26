USE SalesDB

SELECT
OrderID,
Sales,
NTILE(1) OVER (ORDER BY Sales DESC) OneBuckets,
NTILE(2) OVER (ORDER BY Sales DESC) TwoBuckets,
NTILE(3) OVER (ORDER BY Sales DESC) ThreeBuckets,
NTILE(4) OVER (ORDER BY Sales DESC) FourBuckets
FROM Sales.Orders





