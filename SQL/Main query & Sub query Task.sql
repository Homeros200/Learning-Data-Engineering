USE SalesDB

/*Task: Find the product that have a price
        higher than the average price of all proucts*/

SELECT
*
FROM(
    --Subquery 
    SELECT
    ProductID,
    Price,
    AVG(Price) Over() AvgPrice
    FROM Sales.Products
    ) t
WHERE Price > AvgPrice


