USE SalesDB

--Find the products that have a price higher than the average price of all products 

SELECT 
ProductID,
Price,
(SELECT AVG(Price) FROM Sales.Products) AvgPrice
FROM Sales.Products

WHERE Price > (SELECT AVG(Price) FROM Sales.Products)