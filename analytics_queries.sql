-- total revenue
SELECT 
    SUM(total_price) AS total_revenue
FROM order_items;

-- top selling products
SELECT 
    product_id,
    COUNT(*) AS total_sales,
    SUM(total_price) AS revenue
FROM order_items
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

-- revenue per seller
SELECT 
    seller_id,
    COUNT(*) AS orders,
    SUM(total_price) AS revenue
FROM order_items
GROUP BY seller_id
ORDER BY revenue DESC;

-- average order value
SELECT 
    AVG(total_price) AS avg_order_value
FROM order_items;

-- seller performance rank
SELECT
    seller_id,
    SUM(total_price) AS revenue,
    RANK() OVER (ORDER BY SUM(total_price) DESC) AS seller_rank
FROM order_items
GROUP BY seller_id;

-- product sales distribution
SELECT 
    product_id,
    COUNT(*) AS total_orders
FROM order_items
GROUP BY product_id
ORDER BY total_orders DESC;

-- shipping cost analysis
SELECT
    AVG(freight_value) AS avg_shipping_cost,
    MAX(freight_value) AS max_shipping_cost
FROM order_items;