-- INSERTION DES DIMENSIONS

-- Produits
INSERT INTO dim_products (stock_code, description)
SELECT DISTINCT stockcode, description
FROM raw_transactions
WHERE stockcode IS NOT NULL AND description IS NOT NULL
ON CONFLICT (stock_code) DO NOTHING;

-- Clients
INSERT INTO dim_customers (customer_id, country)
SELECT DISTINCT customerid, country
FROM raw_transactions
WHERE customerid IS NOT NULL AND country IS NOT NULL
ON CONFLICT (customer_id) DO NOTHING;

-- Temps
INSERT INTO dim_time (date_key, year, month, day, weekday)
SELECT DISTINCT
    CAST(invoicedate AS DATE) AS date_key,
    EXTRACT(YEAR FROM invoicedate) AS year,
    EXTRACT(MONTH FROM invoicedate) AS month,
    EXTRACT(DAY FROM invoicedate) AS day,
    TRIM(TO_CHAR(invoicedate, 'Day')) AS weekday
FROM raw_transactions
WHERE invoicedate IS NOT NULL
ON CONFLICT (date_key) DO NOTHING;
