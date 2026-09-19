CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    price FLOAT NOT NULL,
    entry_date TEXT NOT NULL,
    brand VARCHAR(10) NOT NULL,
    stock_available SMALLINT NOT NULL
);


CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date TEXT NOT NULL,
    buyer_email VARCHAR(15) NOT NULL,
    total_amount FLOAT NOT NULL
);

CREATE TABLE products_per_invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantity INTEGER NOT NULL,
    total_amount FLOAT NOT NULL,
    
    id_product INTEGER REFERENCES products(id),
    id_invoice INTEGER REFERENCES invoices(id)
);

CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email VARCHAR(10) NOT NULL
);

CREATE TABLE shopping_cart_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    id_shopping_cart INTEGER REFERENCES shopping_cart(id),
    id_product INTEGER REFERENCES products(id)
);

