-- Define Stored Procedure
ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS 
BEGIN 

DECLARE @TotalCustomers INT, @AvgScore FLOAT;

SELECT
	@TotalCustomers = COUNT(*) ,
	@AvgScore = AVG(Score)
FROM Sales.Customers
WHERE Country = @Country;

PRINT 'Total Customers from ' + @Country + ': ' +  CAST(@TotalCustomers AS NVARCHAR);
PRINT 'Average Score from' + @Country  + ': ' + CAST(@AvgScore AS NVARCHAR);

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




