SELECT 
OrderID,
Sales,
Quantity,
Sales / NULLIF(Quantity,0) AS Singleprice

From Sales.Orders







