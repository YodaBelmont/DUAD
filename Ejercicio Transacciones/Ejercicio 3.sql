SET search_path TO "EjercicioTransacciones";

DO $$
DECLARE
	v_bill_id INTEGER;
	

BEGIN
	--VERIFICAR QUE LA FACTURA EXISTE
	SELECT id INTO v_bill_id
	FROM bills
	WHERE id = 1;

	IF v_bill_id IS NULL THEN
		RAISE EXCEPTION 'BILL ID NOT FOUND';
	END IF;

	--ACTUALIZAR EL STOCK
	UPDATE products
	SET quantity = quantity +1
	WHERE id IN (1, 2);

	--MODIFICAR FACTURA ORIGINAL

	UPDATE bills
	SET state = 'returned'
	WHERE id = 1;

	RAISE NOTICE 'TRANSACCTION SUCCESS';

END $$

	