
CREATE TABLE Electric_Vehicle_Sales (
    Year INT,
    Month_Name VARCHAR(10),
    Date DATE,
    State VARCHAR(100),
    Vehicle_Class VARCHAR(100),
    Vehicle_Category VARCHAR(100),
    Vehicle_Type VARCHAR(100),
    EV_Sales_Quantity INT
);
copy Electric_Vehicle_Sales(Year,Month_Name,Date,State,Vehicle_Class,Vehicle_Category,Vehicle_Type,EV_Sales_Quantity)
from 'C:\Users\Public\electric vehicle sales\Cleaned_Electric_Vehicle_Sales2.csv'
DELIMITER ','
CSV HEADER;

select * from Electric_Vehicle_Sales;

SELECT * FROM Electric_Vehicle_Sales LIMIT 10;

-- Total EV sales
SELECT SUM(EV_Sales_Quantity) AS Total_Sales FROM Electric_Vehicle_Sales;

-- Year-wise total sales
SELECT Year, SUM(EV_Sales_Quantity) AS Yearly_Sales
FROM Electric_Vehicle_Sales
GROUP BY Year
ORDER BY Year;

-- State-wise total sales
SELECT State, SUM(EV_Sales_Quantity) AS Total_Sales
FROM Electric_Vehicle_Sales
GROUP BY State
ORDER BY Total_Sales DESC;

-- Vehicle type-wise total
SELECT Vehicle_Type, SUM(EV_Sales_Quantity) AS Type_Sales
FROM Electric_Vehicle_Sales
GROUP BY Vehicle_Type
ORDER BY Type_Sales DESC;

-- Vehicle class-wise total
SELECT Vehicle_Class, SUM(EV_Sales_Quantity) AS Class_Sales
FROM Electric_Vehicle_Sales
GROUP BY Vehicle_Class
ORDER BY Class_Sales DESC;

-- Month-wise sales trend
SELECT Month_Name, SUM(EV_Sales_Quantity) AS Monthly_Sales
FROM Electric_Vehicle_Sales
GROUP BY Month_Name
ORDER BY 
    CASE 
        WHEN Month_Name = 'Jan' THEN 1
        WHEN Month_Name = 'Feb' THEN 2
        WHEN Month_Name = 'Mar' THEN 3
        WHEN Month_Name = 'Apr' THEN 4
        WHEN Month_Name = 'May' THEN 5
        WHEN Month_Name = 'Jun' THEN 6
        WHEN Month_Name = 'Jul' THEN 7
        WHEN Month_Name = 'Aug' THEN 8
        WHEN Month_Name = 'Sep' THEN 9
        WHEN Month_Name = 'Oct' THEN 10
        WHEN Month_Name = 'Nov' THEN 11
        WHEN Month_Name = 'Dec' THEN 12
    END;

-- Highest selling year
SELECT Year, SUM(EV_Sales_Quantity) AS Total_Sales
FROM Electric_Vehicle_Sales
GROUP BY Year
ORDER BY Total_Sales DESC
LIMIT 1;

-- Top 5 states by sales
SELECT State, SUM(EV_Sales_Quantity) AS Total_Sales
FROM Electric_Vehicle_Sales
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 5;

-- Compare 2W vs 4W
SELECT Vehicle_Type, SUM(EV_Sales_Quantity) AS Total_Sales
FROM Electric_Vehicle_Sales
WHERE Vehicle_Type IN ('2W_Personal', '4W_Personal')
GROUP BY Vehicle_Type;

-- Average EV sales per state
SELECT State, ROUND(AVG(EV_Sales_Quantity), 2) AS Avg_Sales
FROM Electric_Vehicle_Sales
GROUP BY State
ORDER BY Avg_Sales DESC;

-- State and year-wise sales
SELECT State, Year, SUM(EV_Sales_Quantity) AS Total_Sales
FROM Electric_Vehicle_Sales
GROUP BY State, Year
ORDER BY State, Year;

-- Minimum and maximum EV sales
SELECT MIN(EV_Sales_Quantity) AS Min_Sales, MAX(EV_Sales_Quantity) AS Max_Sales
FROM Electric_Vehicle_Sales;

-- Vehicle category-wise sales
SELECT Vehicle_Category, SUM(EV_Sales_Quantity) AS Total_Sales
FROM Electric_Vehicle_Sales
GROUP BY Vehicle_Category
ORDER BY Total_Sales DESC;