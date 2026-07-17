-- Define Stored Procedure
ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS 
BEGIN 
SELECT
COUNT(*) TotalCustomers,
AVG(Score) AvgScore,
@Country AS Country
FROM Sales.Customers
WHERE Country = @Country
END

-- Execute the Stored Procedure
EXEC GetCustomerSummary @Country = 'Germany'

EXEC GetCustomerSummary

