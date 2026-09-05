-- CREATE TABLE products (
--     id INT PRIMARY KEY,
--     name VARCHAR(10) NOT NULL,
--     price FLOAT NOT NULL,
--     entry_date TEXT NOT NULL,
--     brand VARCHAR(10) NOT NULL,
--     stock_available SMALLINT NOT NULL
-- );

-- CREATE TABLE invoices (
--     invoice_number INT PRIMARY KEY,
--     purchase_date TEXT NOT NULL,
--     buyer_email VARCHAR(15) NOT NULL,
--     total_amount FLOAT NOT NULL
-- );

-- CREATE TABLE products_per_invoice (
--     id INT PRIMARY KEY,
--     quantity INT NOT NULL,
--     total_amount INT NOT NULL,
    
--     id_product INT REFERENCES products(id),
--     id_invoice INT REFERENCES invoices(invoice_number)
-- );

-- CREATE TABLE shopping_cart (
--     shopping_cart_id INT PRIMARY KEY,
--     buyer_email VARCHAR(10) NOT NULL
-- );

-- CREATE TABLE shopping_cart_products (
--     id INT PRIMARY KEY,

--     id_shopping_cart INT REFERENCES shopping_cart(shopping_cart_id),
--     id_product INT REFERENCES products(id)
-- );
