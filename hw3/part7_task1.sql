SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    country,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM Customers AS c
INNER JOIN Orders AS o
    ON c.customer_id = o.customer_id
INNER JOIN Shippings AS s
    ON c.customer_id = s.customer
WHERE status = 'Delivered'
GROUP BY c.customer_id, c.first_name, c.last_name, c.country
HAVING COUNT(order_id) > 1
