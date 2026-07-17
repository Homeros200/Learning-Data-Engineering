-- Define Stored Procedure
ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS 
BEGIN 
SELECT
COUNT(*) TotalCustomers,
AVG(Score) AvgScore,
@Country AS Country
FROM Sales.Customers
WHERE Country = @Country;

-- Find the total Nr. of Orders and Total Sales
SELECT 
COUNT(OrderID) TotalOrders,
SUM(Sales) TotalSales
FROM Sales.Orders o
JOIN Sales.Customers c
ON c.CustomerID = o.CustomerID
WHERE c.Country = @Country;

END

-- Execute the Stored Procedure
EXEC GetCustomerSummary @Country = 'Germany'

EXEC GetCustomerSummary




