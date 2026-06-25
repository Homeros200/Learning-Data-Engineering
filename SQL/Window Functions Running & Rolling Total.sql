--Calculate moving average of sales for each product over time
--Calculate moving average of sales for each product over time,including only the next order

USE SalesDB

SELECT
OrderID,
ProductID,
OrderDate,
Sales,
AVG(Sales) OVER (PARTITION BY ProductID) AvgByProduct,
AVG(Sales) OVER (PARTITION BY ProductID ORDER BY OrderDate) MovingAvg,
AVG(Sales) OVER (PARTITION BY ProductID ORDER BY OrderDate ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING  ) RollingAVG
FROM Sales.Orders