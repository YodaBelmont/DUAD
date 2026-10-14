
SET search_path TO "EjercicioTransacciones";

DO $$
DECLARE
	v_bill_id INTEGER = 1;
	
BEGIN
	-- CONFIRMAR QUE LA FACTURA EXISTE
	
	IF NOT EXISTS(
		SELECT 1
		FROM Bills
		WHERE id = v_bill_id
		AND state = 'paid'
	) THEN
		RAISE EXCEPTION 'BILL DOES NOT EXISTS // ALREADY RETURNED';
	END IF;

	--ACTUALIZA STOCK
	
	UPDATE Products AS p
	SET quantity = p.quantity + pb.quantity
	FROM Products_bills AS pb
	WHERE p.id = pb.product_id
	AND pb.bill_id = v_bill_id;

	--MODIFICAR FACTURA ORIGINAL

	UPDATE bills
	SET state = 'returned'
	WHERE id = v_bill_id;

	RAISE NOTICE 'TRANSACCTION SUCCESS';

END $$

	