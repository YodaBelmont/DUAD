SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS Cars;

CREATE TABLE Cars(
	id SERIAL PRIMARY KEY,
	brand VARCHAR(20) NOT NULL,
	model VARCHAR(25) NOT NULL,
	year INTEGER NOT NULL,
	state VARCHAR(20) NOT NULL
);

INSERT INTO Cars (brand, model, year, state)
VALUES
('Toyota', 'Corolla', 2020, 'available'),
('Honda', 'Civic', 2019, 'rented'),
('Hyundai', 'Elantra', 2021, 'available'),
('Nissan', 'Sentra', 2018, 'maintenance'),
('Kia', 'Rio', 2022, 'available'),
('Ford', 'Focus', 2017, 'rented'),
('Chevrolet', 'Spark', 2020, 'available'),
('Mazda', 'Mazda3', 2023, 'available'),
('Volkswagen', 'Jetta', 2019, 'rented'),
('Suzuki', 'Swift', 2021, 'available'),

('Toyota', 'RAV4', 2022, 'available'),
('Honda', 'CR-V', 2020, 'rented'),
('Hyundai', 'Tucson', 2023, 'available'),
('Nissan', 'X-Trail', 2019, 'maintenance'),
('Kia', 'Sportage', 2021, 'available'),
('Ford', 'Escape', 2018, 'rented'),
('Chevrolet', 'Tracker', 2022, 'available'),
('Mazda', 'CX-5', 2020, 'available'),
('Volkswagen', 'Tiguan', 2023, 'rented'),
('Suzuki', 'Vitara', 2017, 'available'),

('Toyota', 'Hilux', 2021, 'available'),
('Ford', 'Ranger', 2022, 'rented'),
('Nissan', 'Frontier', 2020, 'available'),
('Mitsubishi', 'L200', 2019, 'maintenance'),
('Isuzu', 'D-Max', 2023, 'available'),
('Chevrolet', 'Colorado', 2021, 'rented'),
('Toyota', 'Tacoma', 2018, 'available'),
('Ford', 'F-150', 2024, 'available'),
('Ram', '1500', 2022, 'rented'),
('Nissan', 'Navara', 2020, 'available'),

('BMW', '320i', 2021, 'available'),
('Mercedes-Benz', 'C200', 2022, 'rented'),
('Audi', 'A4', 2020, 'available'),
('Lexus', 'IS300', 2019, 'maintenance'),
('Volvo', 'S60', 2023, 'available'),
('BMW', 'X3', 2021, 'rented'),
('Mercedes-Benz', 'GLA200', 2022, 'available'),
('Audi', 'Q5', 2024, 'available'),
('Lexus', 'RX350', 2020, 'rented'),
('Volvo', 'XC60', 2023, 'available'),

('Toyota', 'Yaris', 2016, 'available'),
('Honda', 'Fit', 2015, 'rented'),
('Hyundai', 'Accent', 2018, 'available'),
('Nissan', 'Versa', 2017, 'maintenance'),
('Kia', 'Picanto', 2020, 'available'),
('Suzuki', 'Celerio', 2019, 'rented'),
('Chevrolet', 'Aveo', 2016, 'available'),
('Mitsubishi', 'Mirage', 2021, 'available'),
('Volkswagen', 'Polo', 2022, 'rented'),
('Mazda', 'Mazda2', 2023, 'available');