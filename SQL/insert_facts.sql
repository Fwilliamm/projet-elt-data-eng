-- INSERTION DE LA TABLE DE FAITS: transaction_details

INSERT INTO transaction_details (
    invoice_no,
    stock_code,
    quantity,
    unit_price,
    total_price,
    invoice_date,
    customer_id,
    date_key
)
SELECT
    invoiceno,
    stockcode,
    quantity,
    unitprice,
    quantity * unitprice AS total_price,
    invoicedate,
    customerid,
    CAST(invoicedate AS DATE) AS date_key
FROM raw_transactions
WHERE
    stockcode IS NOT NULL AND
    quantity IS NOT NULL AND
    unitprice IS NOT NULL AND
    invoicedate IS NOT NULL AND
    customerid IS NOT NULL;
