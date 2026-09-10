-- INSERT INTO products(name, price, entry_date, brand, stock_available)
--     VALUES('Laptop', 500, '3/9/2029', 'Dell', 10);

-- INSERT INTO products(name, price, entry_date, brand, stock_available)
--     VALUES('Mouse', 100, '2/9/2029', 'LogiTech', 5);

-- INSERT INTO products(name, price, entry_date, brand, stock_available)
--     VALUES('Ipad', 300, '1/9/2029', 'Apple', 15);

-- INSERT INTO products(name, price, entry_date, brand, stock_available)
-- VALUES('Keyboard', 80, '4/9/2029', 'LogiTech', 8);

-- INSERT INTO products(name, price, entry_date, brand, stock_available)
-- VALUES('Monitor', 250, '5/9/2029', 'Samsung', 6);

-- INSERT INTO products(name, price, entry_date, brand, stock_available)
-- VALUES('Headset', 120, '6/9/2029', 'Sony', 12);

-- INSERT INTO products(name, price, entry_date, brand, stock_available)
-- VALUES('Webcam', 90, '7/9/2029', 'LogiTech', 7);


-- INSERT INTO invoices(purchase_date, buyer_email, total_amount)
-- VALUES('8/9/2029', 'juan@mail.com', 600);

-- INSERT INTO invoices(purchase_date, buyer_email, total_amount)
-- VALUES('9/9/2029', 'ana@mail.com', 330);

-- INSERT INTO invoices(purchase_date, buyer_email, total_amount)
-- VALUES('10/9/2029', 'carlos@mail.com', 450);

-- INSERT INTO invoices(purchase_date, buyer_email, total_amount)
-- VALUES('11/9/2029', 'maria@mail.com', 200);

-- INSERT INTO invoices(purchase_date, buyer_email, total_amount, buyer_phone_number, employee_id)
-- VALUES('0/9/2029', 'juan@mail.com', 90000.0, '777-777', 8811);

-- INSERT INTO invoices(purchase_date, buyer_email, total_amount, buyer_phone_number, employee_id)
-- VALUES('0/9/2029', 'juan@mail.com', 50000.0, '777-777', 8811);

-- INSERT INTO invoices(purchase_date, buyer_email, total_amount, buyer_phone_number, employee_id)
-- VALUES('0/9/2029', 'juan@mail.com', 80000.0, '777-777', 9977);


-- UPDATE invoices
-- SET purchase_date = '1/9/2029'
-- WHERE id = 5;

-- UPDATE invoices
-- SET purchase_date = '4/9/2029'
-- WHERE id = 6;

-- UPDATE invoices
-- SET purchase_date = '6/9/2029'
-- WHERE id = 7;


-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(3, 500, 1, 1001);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(5, 100, 2, 1001);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(2, 300, 3, 1002);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(4, 100, 2, 1002);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(5, 250, 5, 1003);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(5, 80, 4, 1003);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(3, 100, 2, 1003);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(4, 120, 6, 1004);

-- INSERT INTO products_per_invoice(quantity, total_amount, id_product, id_invoice)
-- VALUES(6, 90, 7, 1004);

-- UPDATE products_per_invoice
-- SET total_amount = 80000
-- WHERE id = 1;

-- UPDATE products_per_invoice
-- SET total_amount = 90000
-- WHERE id = 2;

-- UPDATE products_per_invoice
-- SET total_amount = 50000
-- WHERE id = 3;

-- UPDATE products_per_invoice
-- SET total_amount = 60000
-- WHERE id = 4;

-- UPDATE products_per_invoice
-- SET total_amount = 30000
-- WHERE id = 5;

-- UPDATE products_per_invoice
-- SET total_amount = 20000
-- WHERE id = 6;

-- UPDATE products_per_invoice
-- SET total_amount = 15000
-- WHERE id = 7;

-- UPDATE products_per_invoice
-- SET total_amount = 35000
-- WHERE id = 8;

-- UPDATE products_per_invoice
-- SET total_amount = 70000
-- WHERE id = 9;

-- INSERT INTO shopping_cart(id, buyer_email)
-- VALUES(1, 'juan@mail.com');

-- INSERT INTO shopping_cart(id, buyer_email)
-- VALUES(2, 'ana@mail.com');

-- INSERT INTO shopping_cart(id, buyer_email)
-- VALUES(3, 'carlos@mail.com');

-- INSERT INTO shopping_cart(id, buyer_email)
-- VALUES(4, 'maria@mail.com');

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(1, 1, 1);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(2, 1, 2);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(3, 2, 3);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(4, 2, 6);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(5, 3, 5);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(6, 3, 4);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(7, 3, 2);

-- INSERT INTO shopping_cart_products(id, id_shopping_cart, id_product)
-- VALUES(8, 4, 7);

-- UPDATE invoices
-- SET buyer_phone_number = '888-888'
-- WHERE id = 1;

-- UPDATE invoices
-- SET buyer_phone_number = '777-777'
-- WHERE id IN (1, 2);

-- UPDATE invoices
-- SET buyer_phone_number = '666-666'
-- WHERE id IN (3, 4);

-- UPDATE invoices
-- SET employee_id = 1155
-- WHERE id IN (1, 2);

-- UPDATE invoices
-- SET employee_id = 5511
-- WHERE id IN (3, 4);

-- UPDATE products
-- SET price = 80000
-- WHERE id = 1;

-- UPDATE products
-- SET price = 10000
-- WHERE id = 2;

-- UPDATE products
-- SET price = 25000
-- WHERE id = 3;

-- UPDATE products
-- SET price = 4000
-- WHERE id = 4;

-- UPDATE products
-- SET price = 30000
-- WHERE id = 5;

-- UPDATE products
-- SET price = 15000
-- WHERE id = 6;

-- UPDATE products
-- SET price = 12000
-- WHERE id = 7;

-- UPDATE products_per_invoice
-- SET total_amount = 240000
-- WHERE id = 1;

-- UPDATE products_per_invoice
-- SET total_amount = 50000
-- WHERE id = 2;

-- UPDATE products_per_invoice
-- SET total_amount = 50000
-- WHERE id = 3;

-- UPDATE products_per_invoice
-- SET total_amount = 40000
-- WHERE id = 4;

-- UPDATE products_per_invoice
-- SET total_amount = 150000
-- WHERE id = 5;

-- UPDATE products_per_invoice
-- SET total_amount = 20000
-- WHERE id = 6;

-- UPDATE products_per_invoice
-- SET total_amount = 30000
-- WHERE id = 7;

-- UPDATE products_per_invoice
-- SET total_amount = 60000
-- WHERE id = 8;

-- UPDATE products_per_invoice
-- SET total_amount = 72000
-- WHERE id = 9;

-- UPDATE invoices
-- SET total_amount = 290000
-- WHERE id = 1;

-- UPDATE invoices
-- SET total_amount = 90000
-- WHERE id = 2;

-- UPDATE invoices
-- SET total_amount = 200000
-- WHERE id = 3;

-- UPDATE invoices
-- SET total_amount = 132000
-- WHERE id = 4;

-- UPDATE shopping_cart_products
-- SET id_product = 2
-- WHERE id = 4;

-- UPDATE shopping_cart_products
-- SET id_product = 6
-- WHERE id = 8;

-- UPDATE products_per_invoice
-- SET id_invoice = 1
-- WHERE id_invoice = 1001;

-- UPDATE products_per_invoice
-- SET id_invoice = 2
-- WHERE id_invoice = 1002;

-- UPDATE products_per_invoice
-- SET id_invoice = 3
-- WHERE id_invoice = 1003;

-- UPDATE products_per_invoice
-- SET id_invoice = 4
-- WHERE id_invoice = 1004;