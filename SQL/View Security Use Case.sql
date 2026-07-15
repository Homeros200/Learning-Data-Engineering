-- Provide a view from EU Sales Team
-- that combines details from All tables
-- And Excludes Data related to the USA
CREATE VIEW Sales.V_Order_Details_EU AS(
SELECT
o.OrderID,
o.OrderDate,
p.Product,
p.Category,
COALESCE(c.FirstName,'') + ' ' + COALESCE(c.LastName,'') CustomerName,
c.Country CustomerCountry,
COALESCE(e.FIrstName,'') + ' ' + COALESCE(e.LastName,'') SalesName,
e.Department,
o.Sales,
o.Quantity
FROM Sales.ORders o
LEFT JOIN Sales.Products p
ON p.ProductID = o.ProductID
LEFT JOIN Sales.Customers c
ON c.CUstomerID = o.CustomerID
LEFT JOIN Sales.Employees e
ON e.EmployeeID = o.SalesPersonID
WHERE c.Country != 'USA'
)