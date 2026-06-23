-- Find the total sales across all orders
--Find the total sales for each product
--Find the total sales for each combination of product and order status
--Additionally provide details such order Id, order date


SELECT
OrderID,
OrderDate,
ProductID,
OrderStatus,
Sales,
SUM(Sales) OVER() TotalSales,
SUM(Sales) OVER(PARTITION BY ProductID) TotalSalesByProducts,
SUM(Sales) OVER (PARTITION BY ProductID, OrderStatus) SalesByProductsAndStatus
FROM Sales.Orders




