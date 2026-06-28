USE SalesDB

-- Show all customer details and find the total orders of each customer


--Main Query
SELECT
*
FROM Sales.Customers c
LEFT JOIN (
	SELECT 
	CustomerID,
	COUNT(*) TotalOrders
	FROM Sales.Orders
	GROUP BY CustomerID
	) o
ON c.CustomerID = O.CustomerID



