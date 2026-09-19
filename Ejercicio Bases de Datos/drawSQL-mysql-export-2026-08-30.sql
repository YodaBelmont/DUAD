CREATE TABLE `Products`(
    `Code` INT NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` FLOAT(53) NOT NULL,
    `Entry date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock Avalable` BIGINT NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Invoices`(
    `Invoice Number` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase Date` DATE NOT NULL,
    `Buyer Email` VARCHAR(255) NOT NULL,
    `Total Amount` FLOAT(53) NOT NULL
);
CREATE TABLE `Products Per Invoice`(
    `Id` BIGINT NOT NULL,
    `Quantity` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Total amount` FLOAT(53) NOT NULL,
    `Id Product` BIGINT NOT NULL,
    `Id Invoice` BIGINT NOT NULL,
    PRIMARY KEY(`Id`)
);
CREATE TABLE `Shopping Cart`(
    `Shopping Cart id` BIGINT NOT NULL,
    `Buyer Email` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Shopping Cart id`)
);
CREATE TABLE `Shopping Cart Products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id Shopping Cart` BIGINT NOT NULL,
    `id Products` BIGINT NOT NULL
);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_id product_foreign` FOREIGN KEY(`Id Product`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_id invoice_foreign` FOREIGN KEY(`Id Invoice`) REFERENCES `Invoices`(`Invoice Number`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_code_foreign` FOREIGN KEY(`Code`) REFERENCES `Shopping Cart Products`(`id Products`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_shopping cart id_foreign` FOREIGN KEY(`Shopping Cart id`) REFERENCES `Shopping Cart Products`(`id Shopping Cart`);