--Retruve employee details with gender displayed as full text

SELECT
EmployeeID,
FirstName,
LastName,
Gender,
CASE 
    WHEN Gender = 'M' THEN 'Male'
    WHEN Gender = 'F' THEN 'Female'
    ELSE 'Not Available'
END GenderFullText
FROM Sales.Employees