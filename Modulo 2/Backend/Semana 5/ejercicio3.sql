DO $$
	DECLARE 
		factura_id INTEGER = 1;
		v_factura_exists INTEGER;
		v_producto_id INTEGER;
		v_quantity_factura INTEGER;
	BEGIN
		--Verificar que la factura existe en la base de datos.
		SELECT COUNT(*) INTO v_factura_exists
		FROM lyfter_transacciones.facturas
		WHERE id = factura_id;
	
		IF v_factura_exists = 0 THEN
			RAISE EXCEPTION 'La factura no existe. Abortando transacción.';
		END IF;
		
		--Aumentar el stock del producto en la cantidad que se registró en la compra.
		SELECT producto_id, quantity INTO v_producto_id, v_quantity_factura
		FROM lyfter_transacciones.factura_items
		WHERE facturas_id = factura_id;
	
		UPDATE lyfter_transacciones.productos
		SET stock = stock + v_quantity_factura
		WHERE id = v_producto_id;
		
		UPDATE lyfter_transacciones.factura_items
		SET status = 'Retornado'
		WHERE facturas_id = factura_id;
	
		--Modificar la factura original para marcarla con el estado de "Retornada".
		UPDATE lyfter_transacciones.facturas
		SET status = 'Retornada'
		WHERE id = factura_id;
	
END $$;