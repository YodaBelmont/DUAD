
SET search_path TO "EjercicioTransacciones";



DELETE FROM Users;
DELETE FROM Products;
DELETE FROM User_products;

INSERT INTO Users (username, password)
VALUES
    ('juan123', 'pass123'),
    ('maria456', 'pass456'),
    ('carlos789', 'pass789'),
    ('ana321', 'pass321'),
    ('pedro654', 'pass654');



INSERT INTO Products (name, price, quantity)
VALUES
    ('Laptop', 80000, 10),
    ('Mouse', 5000, 25),
    ('Keyboard', 12000, 15),
    ('Monitor', 45000, 8),
    ('Headphones', 15000, 20),
    ('Webcam', 18000, 5),
    ('USB Cable', 3000, 30),
    ('Microphone', 25000, 3);


INSERT INTO User_products (user_id, product_id, quantity)
VALUES
    --carrito de juan
    (1, 1, 2),
    (1, 2, 3),
    (1, 3, 1),

    --compras de maria
    (2, 4, 2),
    (2, 5, 4),
    (2, 6, 1),

    --compras de carlos
    (3, 1, 15),
    (3, 7, 5),
    (3, 8, 4);