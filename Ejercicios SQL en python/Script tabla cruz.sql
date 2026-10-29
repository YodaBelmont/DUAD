


SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS User_car_rent;

CREATE TABLE User_car_rent(
	id SERIAL PRIMARY KEY,
	user_id INTEGER NOT NULL,
	car_id INTEGER NOT NULL,
	rental_date DATE NOT NULL,
	state VARCHAR(20) NOT NULL,

	FOREIGN KEY (user_id) REFERENCES Users(id),
	FOREIGN KEY (car_id) REFERENCES Cars(id)
);

INSERT INTO User_car_rent (user_id, car_id, rental_date, state)
VALUES
(1, 12, '2026-01-05', 'completed'),
(2, 5, '2026-01-10', 'completed'),
(3, 28, '2026-01-15', 'completed'),
(4, 17, '2026-01-22', 'cancelled'),
(5, 3, '2026-02-01', 'completed'),
(6, 41, '2026-02-05', 'completed'),
(7, 9, '2026-02-10', 'completed'),
(8, 22, '2026-02-18', 'cancelled'),
(9, 35, '2026-02-23', 'completed'),
(10, 14, '2026-03-01', 'completed'),

(11, 47, '2026-03-05', 'completed'),
(12, 6, '2026-03-10', 'completed'),
(13, 31, '2026-03-15', 'cancelled'),
(14, 19, '2026-03-20', 'completed'),
(15, 2, '2026-03-25', 'completed'),
(16, 44, '2026-04-01', 'completed'),
(17, 25, '2026-04-05', 'completed'),
(18, 11, '2026-04-10', 'cancelled'),
(19, 38, '2026-04-15', 'completed'),
(20, 7, '2026-04-20', 'completed'),

(21, 50, '2026-05-01', 'completed'),
(22, 16, '2026-05-05', 'completed'),
(23, 33, '2026-05-10', 'cancelled'),
(24, 4, '2026-05-15', 'completed'),
(25, 27, '2026-05-20', 'completed'),
(26, 10, '2026-06-01', 'completed'),
(27, 43, '2026-06-05', 'completed'),
(28, 21, '2026-06-10', 'cancelled'),
(29, 36, '2026-06-15', 'completed'),
(30, 8, '2026-06-20', 'completed'),

(31, 45, '2026-07-01', 'completed'),
(32, 13, '2026-07-05', 'completed'),
(33, 30, '2026-07-10', 'completed'),
(34, 1, '2026-07-15', 'cancelled'),
(35, 48, '2026-07-20', 'completed'),
(36, 24, '2026-08-01', 'completed'),
(37, 39, '2026-08-05', 'completed'),
(38, 15, '2026-08-10', 'completed'),
(39, 46, '2026-08-15', 'cancelled'),
(40, 20, '2026-08-20', 'completed'),

(41, 34, '2026-09-01', 'completed'),
(42, 18, '2026-09-05', 'completed'),
(43, 49, '2026-09-10', 'completed'),
(44, 26, '2026-09-15', 'cancelled'),
(45, 40, '2026-09-20', 'completed'),
(46, 23, '2026-10-01', 'completed'),
(47, 37, '2026-10-05', 'completed'),
(48, 29, '2026-10-10', 'active'),
(49, 42, '2026-10-15', 'active'),
(50, 32, '2026-10-20', 'active');