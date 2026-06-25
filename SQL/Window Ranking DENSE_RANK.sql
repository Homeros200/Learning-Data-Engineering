USE SalesDB

--Rank the orders based on their sales from highest to lowest

SELECT 
OrderID,
ProductID,
Sales,
DENSE_RANK() OVER(ORDER BY Sales DESC) SalesRank_DenseRank
FROM Sales.Orders