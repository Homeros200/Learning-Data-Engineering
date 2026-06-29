USE SalesDB
--Show the details of orders made by customers in Germany 
--Main Query
SELECT 
*
FROM Sales.Orders
WHERE CUstomerID IN (SELECT CustomerID FROM Sales.Customers WHERE Country = 'Germany')

