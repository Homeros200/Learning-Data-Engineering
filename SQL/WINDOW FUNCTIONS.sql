/*Find the total sales for each product
Additionally provide details such order Id, order date*/
SELECT 
    OrderID,
    OrderDate,
    ProductID,
    SUM(Sales) OVER(partition by ProductID) TotalSales
FROM Sales.Orders
