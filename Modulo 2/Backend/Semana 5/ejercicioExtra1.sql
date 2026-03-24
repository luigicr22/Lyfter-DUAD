DO $$
	DECLARE
		factura_id INTEGER = 1;
		
		v_factura_exists INTEGER;
		v_factura_status character varying(30);
		
		v_producto_id INTEGER;
		v_producto_status character varying(30);
		v_quantity_factura INTEGER;

	BEGIN
		--Verifique que la factura esté en estado "Pendiente"
		SELECT COUNT(*) INTO v_factura_exists
		FROM lyfter_transacciones.facturas
		WHERE id = factura_id;
		
		IF v_factura_exists = 0 THEN
			RAISE EXCEPTION 'La factura no existe. Abortando transacción.';
		END IF;
	
		SELECT status INTO v_factura_status
		FROM lyfter_transacciones.facturas
		WHERE id = factura_id;
	
		IF v_factura_status != 'Pendiente' THEN
			RAISE EXCEPTION 'La factura ya esta entregada. Abortando transacción.';
		END IF;
	
		--Cambie su estado a "Cancelada"
		UPDATE lyfter_transacciones.facturas
		SET status = 'Cancelada'
		WHERE id = factura_id;
			
		--Regrese el stock solo de los productos que aún no han sido entregados
		SELECT producto_id, quantity, status INTO v_producto_id, v_quantity_factura, v_producto_status
		FROM lyfter_transacciones.factura_items
		WHERE facturas_id = factura_id;

		IF v_producto_status != 'Pendiente' THEN
			RAISE EXCEPTION 'Los articulos de la factura ya fueron entregados. Abortando transacción.';
		END IF;

		UPDATE lyfter_transacciones.factura_items
		SET status = 'Cancelada'
		WHERE facturas_id = factura_id;

		UPDATE lyfter_transacciones.productos
		SET stock = stock + v_quantity_factura
		WHERE id = v_producto_id;

END $$;	