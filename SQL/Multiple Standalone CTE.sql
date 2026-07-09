 -- Step1: Find the total Sales Per Customer (Standalone CTE)
 WITH CTE_Total_Sales AS
 (
 SELECT
	CustomerID,
	SUM(Sales) AS TotalSales
FROM Sales.Orders
GROUP BY CustomerID
), CTE_Last_ORder AS
(
SELECT
CustomerID,
MAX(OrderDate) AS Last_Order
FROM Sales.Orders
GROUP BY CustomerID
)
-- STEP2: Find the last order date for each customer
-- Main Query
SELECT
c.CustomerID,
c.FirstName,
c.LastName,
cts.TotalSales,
clo.Last_Order
FROM Sales.Customers c
LEFT JOIN CTE_TOTAL_Sales cts
ON cts.CustomerID = c.CustomerID
LEFT JOIN CTE_Last_Order clo
ON clo.CustomerID = c.CustomerID