USE SalesDB
-- Show the details of orders made by customers in Germany 

-- Main Query
SELECT
*
FROM Sales.Orders o
WHERE EXISTS (SELECT 
				1
				FROM Sales.Customers c
				WHERE Country = 'Germany'
				AND o.CustomerID = c.CustomerID)

SELECT
*
FROM Sales.Orders

SELECT 
*
FROM Sales.Customers









