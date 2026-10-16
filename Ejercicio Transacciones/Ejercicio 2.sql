SET search_path TO "EjercicioTransacciones";

DO $$
DECLARE
	v_bill_id INTEGER;
	v_user_id INTEGER = 1;
	v_total_amount_bill INTEGER;
BEGIN

	-- CONFIRMAR QUE EL USUARIO EXISTE
	IF NOT EXISTS(
		SELECT *
		FROM Users
		WHERE id = v_user_id
	) THEN
		RAISE EXCEPTION 'USER DOES NOT EXISTS';
	END IF;
	
	-- COMPROBAR EXISTENCIAS

	IF EXISTS(
		SELECT 1
		FROM User_products AS up
		INNER JOIN Products AS p
			ON up.product_id = p.id
		WHERE up.user_id = v_user_id
		AND up.quantity > p.quantity
	) THEN
		RAISE EXCEPTION 'NO STOCK AVAILABLE';
	END IF;

	UPDATE Products AS p
	SET quantity = p.quantity - up.quantity
	FROM User_products AS up
	WHERE p.id = up.product_id
	AND up.user_id = v_user_id;
	
	-- INSERTAR FACTURA

	INSERT INTO Bills (date, user_id, state, total_amount)
	VALUES(CURRENT_DATE, v_user_id, 'paid', 0)
	RETURNING id INTO v_bill_id;

	INSERT INTO Products_bills(
		product_id,
		bill_id,
		quantity,
		total_amount
	)
	SELECT
		up.product_id,
		v_bill_id,
		up.quantity,
		p.price * up.quantity
	FROM User_products AS up
	INNER JOIN Products AS p
		ON up.product_id = p.id
	WHERE up.user_id = v_user_id;

	SELECT SUM(p.price * up.quantity)
	INTO v_total_amount_bill
	FROM User_products AS up
	INNER JOIN Products AS p
		ON up.product_id = p.id
	WHERE up.user_id = v_user_id;

	UPDATE Bills
	SET total_amount = v_total_amount_bill
	WHERE id = v_bill_id;
	
	
	--ACTUALIZAR STOCK

	RAISE NOTICE 'TRANSACCTION SUCCESS';
	
	END $$;

	