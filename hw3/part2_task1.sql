SELECT first_name, last_name, item, amount
FROM Customers AS c
INNER JOIN Orders AS o
    ON c.customer_id = o.customer_id;