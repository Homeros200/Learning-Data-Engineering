--Rank Customers based on their total sales

USE SalesDB


SELECT 

RANK() OVER(ORDER BY SUM(Sales) DESC) RankCustomers,
CustomerID,
SUM(Sales) TotalSales

FROM Sales.Orders
GROUP BY customerID


