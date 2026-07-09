 -- Step1: Find the total Sales Per Customer (Standalone CTE)
 WITH CTE_Total_Sales AS
 (
 SELECT
	CustomerID,
	SUM(Sales) AS TotalSales
FROM Sales.Orders
GROUP BY CustomerID
)

-- Step2: Find the last order date for each customer
,CTE_Last_Order As 
(
SELECT 
	CustomerID,
	MAX(OrderDate) AS Last_Order
FROM Sales.Orders
GROUP BY CustomerID
)


-- Step3: Rank Customers based on Total Sales Per Customer
,CTE_Customer_Rank AS
(
SELECT 
CustomerID,
TotalSales,
RANK() OVER (ORDER BY TotalSales DESC) AS CustomerRank
FROM CTE_TOTAL_Sales ccr
)
-- Step4: Segment Customers Based on their Total Sales
, CTE_Customer_Segments AS
(
SELECT
CustomerID,
TotalSales,
CASE WHEN TotalSales > 100 THEN 'High'
	 WHEN TotalSales > 80 THEN 'Medium'
	 ELSE 'Low'
END CustomerSegments
FROM CTE_Total_Sales
)

--Main Query

SELECT
c.CustomerID,
c.FirstName,
c.LastName,
cts.TotalSales,
clo.Last_Order,
ccr.CustomerRank,
ccs.CustomerSegments
From Sales.Customers c
LEFT JOIN CTE_Total_Sales cts
ON cts.CustomerID= c.CustomerID
LEFT JOIN CTE_Last_Order clo
ON clo.CustomerID = c.CustomerID
LEFT JOIN CTE_Customer_Rank ccr
ON ccr.CustomerID = c.CustomerID
LEFT JOIN CTE_Customer_Segments ccs
ON ccs.CustomerID = c.CustomerID