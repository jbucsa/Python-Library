SELECT 
    YEAR(o.orderdate) AS year,
    MONTH(o.orderdate) AS month,
    o.customerid,
    SUM(od.unitprice * od.quantity) AS total_monthly_order_value
FROM orders o
JOIN order_details od ON o.orderid = od.orderid
GROUP BY year, month, o.customerid
HAVING total_monthly_order_value = (
    SELECT MAX(total_value) 
    FROM (
        SELECT SUM(unitprice * quantity) AS total_value
        FROM orders o_inner
        JOIN order_details od_inner ON o_inner.orderid = od_inner.orderid
        WHERE YEAR(o_inner.orderdate) = year 
        AND MONTH(o_inner.orderdate) = month
        GROUP BY o_inner.customerid
    ) AS max_values
)
ORDER BY year, month;