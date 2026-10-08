
SET search_path TO "EjercicioTransacciones";

DO $$
DECLARE 
	v_stock_available INTEGER;
	v_total_amount INTEGER;
	v_username VARCHAR(20);
BEGIN
	-- COMPROBAR EXISTENCIAS
	SELECT quantity INTO v_stock_available
	FROM products
	WHERE id = 1;

	IF v_stock_available IS NULL OR v_stock_available < 1 THEN
		RAISE EXCEPTION 'OUT OF STOCK FOR PRODUCT_ID = 1';
	END IF;

	SELECT quantity INTO v_stock_available
	FROM products
	WHERE id = 2;

	IF v_stock_available IS NULL OR v_stock_available < 1 THEN
		RAISE EXCEPTION 'OUT OF STOCK FOR PRODUCT_ID = 2';
	END IF;

	-- CONFIRMAR QUE EL USUARIO EXISTE
	SELECT username into v_username
	FROM users
	WHERE username = 'juan123';
	
	IF v_username IS NULL OR v_username != 'juan123' THEN
		RAISE EXCEPTION 'USERNAME NOT FOUND - TRANSACCTION WILL BE CANCELED';
	END IF;
	
	-- INSERTAR FACTURA
	
	INSERT INTO bills (id, date, user_id, state)
	VALUES(1, CURRENT_DATE, 1, 'paid');

	SELECT price * 1 INTO v_total_amount
	FROM products
	WHERE id = 1;

	INSERT INTO products_bills (product_id, bill_id, quantity, total_amount)
	VALUES(1, 1, 1, v_total_amount);

	SELECT price * 1 INTO v_total_amount
	FROM products
	WHERE id = 2;

	INSERT INTO products_bills (product_id, bill_id, quantity, total_amount)
	VALUES(2, 1, 1, v_total_amount);
	
	--ACTUALIZAR STOCK
	
	UPDATE products
	SET quantity = quantity -1
	WHERE id IN (1, 2);

	RAISE NOTICE 'TRANSACCTION SUCCESS';
	
	END $$;

	