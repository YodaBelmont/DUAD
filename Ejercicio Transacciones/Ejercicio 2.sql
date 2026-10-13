SET search_path TO "EjercicioTransacciones";

DO $$
DECLARE 
	v_total_amount INTEGER;
	v_row_product RECORD;
	v_id_row RECORD;
	v_bill_id INTEGER;
BEGIN

	-- CONFIRMAR QUE EL USUARIO EXISTE
	
	FOR v_id_row IN
		SELECT DISTINCT
			u.id AS user_id,
			up.user_id AS cart_user_id
		FROM User_products AS up
		LEFT JOIN Users AS u
			ON up.user_id = u.id
	LOOP
		IF v_id_row.user_id IS NULL THEN
			RAISE EXCEPTION 'USER DOES NOT EXISTS';
		END IF;
		
		INSERT INTO bills (date, user_id, state, total_amount)
		VALUES(CURRENT_DATE, v_id_row.cart_user_id, 'pending', 0);
		RETURNING id INTO v_bill_id;
	END LOOP;
	
	-- COMPROBAR EXISTENCIAS
	
	FOR v_row_product IN 
		SELECT u.id, 
		up.product_id, 
		up.quantity AS requested_quantity,
		p.quantity AS available_stock
		FROM User_products AS up
		
		INNER JOIN Users AS u
			ON up.user_id = u.id
		
		INNER JOIN Products as p
			ON up.product_id = p.id
	LOOP
		IF v_row_product.requested_quantity > v_row_product.available_stock THEN
			RAISE EXCEPTION 'NOT STOCK AVAILABLE - ABORTING TRANSACTION';
		END IF;
			
		UPDATE products
		SET quantity = quantity - v_row_product.requested_quantity
		WHERE id = v_row_product.product_id;
		
	END LOOP;
	
	-- INSERTAR FACTURA
	
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

	RAISE NOTICE 'TRANSACCTION SUCCESS';
	
	END $$;

	