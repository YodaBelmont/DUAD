CREATE TABLE `Products`(
    `Code` INT NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` FLOAT(53) NOT NULL,
    `Entry date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock Avalable` BOOLEAN NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Invoices`(
    `Invoice Number` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase Date` DATE NOT NULL,
    `Buyer Email` VARCHAR(255) NOT NULL,
    `Total Amount` FLOAT(53) NOT NULL
);
CREATE TABLE `Products Per Invoice`(
    `Quantity` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Total amount` INT NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `Buyer Email` VARCHAR(255) NOT NULL,
    `Products` INT NOT NULL,
    `Invoice Id` BIGINT NOT NULL,
    PRIMARY KEY(`Buyer Email`)
);
CREATE TABLE `Shopping Cart Products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id Shopping Cart` BIGINT NOT NULL,
    `id Products` BIGINT NOT NULL
);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_code_foreign` FOREIGN KEY(`Code`) REFERENCES `Shopping Cart Products`(`id Products`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Shopping Cart`(`Invoice Id`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_products_foreign` FOREIGN KEY(`Products`) REFERENCES `Shopping Cart Products`(`id Shopping Cart`);