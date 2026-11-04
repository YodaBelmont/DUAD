SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS User_car_rent;

CREATE TABLE User_car_rent(
	id SERIAL PRIMARY KEY,
	user_id INTEGER NOT NULL,
	car_id INTEGER NOT NULL,
	rental_date DATE DEFAULT CURRENT_DATE,
	state VARCHAR(20) NOT NULL,

	FOREIGN KEY (user_id) REFERENCES Users(id),
	FOREIGN KEY (car_id) REFERENCES Cars(id)
);

INSERT INTO User_car_rent (user_id, car_id, state)
VALUES
(1, 12, 'completed'),
(2, 5, 'completed'),
(3, 28, 'completed'),
(4, 17, 'cancelled'),
(5, 3, 'completed'),
(6, 41, 'completed'),
(7, 9, 'completed'),
(8, 22, 'cancelled'),
(9, 35, 'completed'),
(10, 14, 'completed'),

(11, 47, 'completed'),
(12, 6, 'completed'),
(13, 31, 'cancelled'),
(14, 19, 'completed'),
(15, 2, 'completed'),
(16, 44, 'completed'),
(17, 25, 'completed'),
(18, 11, 'cancelled'),
(19, 38, 'completed'),
(20, 7, 'completed'),

(21, 50, 'completed'),
(22, 16, 'completed'),
(23, 33, 'cancelled'),
(24, 4, 'completed'),
(25, 27, 'completed'),
(26, 10, 'completed'),
(27, 43, 'completed'),
(28, 21, 'cancelled'),
(29, 36, 'completed'),
(30, 8, 'completed'),

(31, 45, 'completed'),
(32, 13, 'completed'),
(33, 30, 'completed'),
(34, 1, 'cancelled'),
(35, 48, 'completed'),
(36, 24, 'completed'),
(37, 39, 'completed'),
(38, 15, 'completed'),
(39, 46, 'cancelled'),
(40, 20, 'completed'),

(41, 34, 'completed'),
(42, 18, 'completed'),
(43, 49, 'completed'),
(44, 26, 'cancelled'),
(45, 40, 'completed'),
(46, 23, 'completed'),
(47, 37, 'completed'),
(48, 29, 'active'),
(49, 42, 'active'),
(50, 32, 'active');