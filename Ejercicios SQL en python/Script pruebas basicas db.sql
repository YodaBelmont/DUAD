
SET search_path TO lyfter_car_rental;

--INSERT INTO Users (name, email, username, password, birth_date, account_status)
--VALUES('Esteban Cayu', 'Estemv@mail.com', 'EsteMV', 'teban12345', '1970-01-10','inactive');

--INSERT INTO Cars (brand, model, year, state)
--VALUES('Honda', 'NSX', 1998, 'available');

--UPDATE Users
--SET account_status = 'active'
--WHERE name = 'Esteban Cayu' AND username = 'EsteMV';

--UPDATE Cars
--SET state = 'rented'
--WHERE id = 51;

--INSERT INTO User_car_rent (user_id, car_id, rental_date, state)
--VALUES (51, 51, CURRENT_DATE, 'active');

--UPDATE User_car_rent
--SET state = 'completed'
--WHERE user_id = 51 AND car_id = 51;

--UPDATE Cars
--SET state = 'available'
--WHERE id = 51;

--UPDATE Cars
--SET state = 'maintenance'
--WHERE id = 51;

--SELECT *
--FROM Cars
--WHERE state = 'rented';

--SELECT *
--FROM Cars
--WHERE state = 'available';

SELECT *
FROM Users




