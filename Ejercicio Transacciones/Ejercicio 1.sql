
SET search_path TO "EjercicioTransacciones";

DROP TABLE IF EXISTS User_products;
DROP TABLE IF EXISTS Products_Bills;
DROP TABLE IF EXISTS Bills;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Products;



CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(10) NOT NULL
);

CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    price INTEGER NOT NULL,
    quantity INTEGER NOT NULL
);

CREATE TABLE User_products (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,

    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES Users(id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES Products(id)
);

CREATE TABLE Bills (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    user_id INTEGER NOT NULL,
    state VARCHAR(10) NOT NULL,
    total_amount INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT fk_bill_user
        FOREIGN KEY (user_id)
        REFERENCES Users(id)
);

CREATE TABLE Products_Bills (
    product_id INTEGER NOT NULL,
    bill_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount INTEGER NOT NULL,

    PRIMARY KEY (product_id, bill_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES Products(id),

    CONSTRAINT fk_bill
        FOREIGN KEY (bill_id)
        REFERENCES Bills(id)
);