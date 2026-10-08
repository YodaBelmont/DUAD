
SET search_path TO "EjercicioTransacciones";


CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(10) NOT NULL
);

CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    price INTEGER NOT NULL,
	quantity INTEGER NOT NULL
);

CREATE TABLE Bills (
    id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    user_id INTEGER NOT NULL,
	ADD COLUMN state VARCHAR(10) NOT NULL

    CONSTRAINT fk_bill_user
        FOREIGN KEY (user_id)
        REFERENCES Users(id)
);

CREATE TABLE Products_Bills (
    product_id INTEGER NOT NULL,
    bill_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL,
	total_amount INTEGER NOT NULL

    PRIMARY KEY (product_id, bill_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES Products(id),

    CONSTRAINT fk_bill
        FOREIGN KEY (bill_id)
        REFERENCES Bills(id)
);