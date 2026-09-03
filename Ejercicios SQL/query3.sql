-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
--     VALUES(1, 'Laptop', 500, '3/9/2029', 'Dell', 10);

-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
--     VALUES(2, 'Mouse', 100, '2/9/2029', 'LogiTech', 5);

-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
--     VALUES(3, 'Ipad', 300, '1/9/2029', 'Apple', 15);

-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
-- VALUES(4, 'Keyboard', 80, '4/9/2029', 'LogiTech', 8);

-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
-- VALUES(5, 'Monitor', 250, '5/9/2029', 'Samsung', 6);

-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
-- VALUES(6, 'Headset', 120, '6/9/2029', 'Sony', 12);

-- INSERT INTO products(id, name, price, entry_date, brand, stock_available)
-- VALUES(7, 'Webcam', 90, '7/9/2029', 'LogiTech', 7);


-- INSERT INTO invoices(invoice_number, purchase_date, buyer_email, total_amount)
-- VALUES(1001, '8/9/2029', 'juan@mail.com', 600);

-- INSERT INTO invoices(invoice_number, purchase_date, buyer_email, total_amount)
-- VALUES(1002, '9/9/2029', 'ana@mail.com', 330);

-- INSERT INTO invoices(invoice_number, purchase_date, buyer_email, total_amount)
-- VALUES(1003, '10/9/2029', 'carlos@mail.com', 450);

-- INSERT INTO invoices(invoice_number, purchase_date, buyer_email, total_amount)
-- VALUES(1004, '11/9/2029', 'maria@mail.com', 200);


-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(1, 1, 500, 1, 1001);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(2, 1, 100, 2, 1001);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(3, 1, 300, 3, 1002);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(4, 1, 100, 2, 1002);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(5, 1, 250, 5, 1003);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(6, 1, 80, 4, 1003);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(7, 1, 100, 2, 1003);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(8, 1, 120, 6, 1004);

-- INSERT INTO products_per_invoice(id, quantity, total_amount, id_product, id_invoice)
-- VALUES(9, 1, 90, 7, 1004);

-- INSERT INTO shopping_cart(shopping_cart_id, buyer_email)
-- VALUES(1, 'juan@mail.com');

-- INSERT INTO shopping_cart(shopping_cart_id, buyer_email)
-- VALUES(2, 'ana@mail.com');

-- INSERT INTO shopping_cart(shopping_cart_id, buyer_email)
-- VALUES(3, 'carlos@mail.com');

-- INSERT INTO shopping_cart(shopping_cart_id, buyer_email)
-- VALUES(4, 'maria@mail.com');

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(1, 1, 1);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(2, 1, 2);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(3, 2, 3);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(4, 2, 6);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(5, 3, 5);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(6, 3, 4);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(7, 3, 2);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_products)
-- VALUES(8, 4, 7);

-- UPDATE invoices
-- SET buyer_phone_number = '888-888'
-- WHERE invoice_number = 1002;

-- UPDATE invoices
-- SET buyer_phone_number = '777-777'
-- WHERE invoice_number = 1003;

-- UPDATE invoices
-- SET buyer_phone_number = '666-666'
-- WHERE invoice_number = 1004;

-- UPDATE invoices
-- SET employee_id = 100
-- WHERE invoice_number = 1001;

-- UPDATE invoices
-- SET employee_id = 200
-- WHERE invoice_number = 1003;

-- UPDATE invoices
-- SET employee_id = 100
-- WHERE invoice_number = 1002;

-- UPDATE invoices
-- SET employee_id = 200
-- WHERE invoice_number = 1004;