SELECT count(*) as delivered_orders_count --Запрос на то, сколько товаров уже доставили
FROM FACT_SALES as fs
JOIN DIM_ORDER do ON fs.order_sk = do.order_sk
WHERE status = 'Доставлен'; --соединили таблицы по order_sk

SELECT count(*) discount_orders_count --Запрос на то, сколько заказов у нас оформили за 2026 год со скидками
FROM FACT_SALES as fs
JOIN DIM_DISCOUNT dd ON fs.discount_sk = dd.discount_sk
JOIN DIM_DATE dda ON fs.date_sk = dda.date_sk --соединили 3 таблицы по общим
WHERE discount_amount > 0 and year = 2026;

SELECT dc.firstname, dc.lastname, SUM(fs.line_total) as total_spent --Узнаем топ 5 покупателей, потративших наибольшее количество денег
FROM FACT_SALES as fs
JOIN DIM_CUSTOMER dc ON fs.customer_sk = dc.customer_sk --соединили таблицы
GROUP BY dc.customer_sk, dc.firstname, dc.lastname --сгруппировали
ORDER BY total_spent DESC --отсортировали по убыванию
LIMIT 5; --только топ 5 выделилили

SELECT dp.category, count(*) as category_orders --узнаем самые продающиеся категории
FROM FACT_SALES as fs
JOIN DIM_PRODUCT dp ON fs.product_sk = dp.product_sk
GROUP BY dp.category
ORDER BY category_orders DESC;

SELECT dc.firstname, dc.lastname, fs.line_total --узнаем клиентов, которые сделали заказ выше среднего чека
FROM FACT_SALES as fs
JOIN DIM_CUSTOMER dc ON fs.customer_sk = dc.customer_sk
WHERE fc.line_total > (SELECT AVG(line_total) FROM FACT_SALES); --через подзапрос узнаем где чек > среднего

SELECT 
    fs.sales_sk,
    dc.firstname,
    dc.lastname,
    fs.line_total,
    SUM(fs.line_total) OVER (PARTITION BY fs.customer_sk) AS customer_total_spent
FROM FACT_SALES as fs
JOIN DIM_CUSTOMER dc ON fs.customer_sk = dc.customer_sk;
/* Добавлю шестым запрос с оконной функцией, если допустим надо увидеть каждого клиента
и отдельной колонкой общую сумму его трат*/
