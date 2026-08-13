SELECT s.status, c.first_name, c.last_name
FROM Shippings AS s
INNER JOIN Customers AS c
    ON s.customer = c.customer_id;
