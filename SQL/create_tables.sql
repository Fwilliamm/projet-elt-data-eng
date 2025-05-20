-- CREATE TABLES: Data Warehouse Retail

--  Table produits
CREATE TABLE IF NOT EXISTS dim_products (
    stock_code TEXT PRIMARY KEY,
    description TEXT
);

--  Table clients
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INTEGER PRIMARY KEY,
    country TEXT
);

--  Table de temps
CREATE TABLE IF NOT EXISTS dim_time (
    date_key DATE PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    weekday TEXT
);

--  Table de faits : transactions de vente
CREATE TABLE IF NOT EXISTS transaction_details (
    invoice_no TEXT,
    stock_code TEXT,
    quantity INTEGER,
    unit_price NUMERIC(10, 2),
    total_price NUMERIC(12, 2),
    invoice_date TIMESTAMP,
    customer_id INTEGER,
    date_key DATE,

--  Clés étrangères
    FOREIGN KEY (stock_code) REFERENCES dim_products(stock_code),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (date_key) REFERENCES dim_time(date_key)
);
