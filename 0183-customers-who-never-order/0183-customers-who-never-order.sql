# Write your MySQL query statement below
SELECT name as Customers
FROM Customers as c
LEFT JOIN (SELECT customerId
        FROM Orders) as o
ON c.id = o.customerId
WHERE customerId is null;