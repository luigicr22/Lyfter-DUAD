DO $$
	DECLARE
		product_to_buy INTEGER = 1;
		quantity_to_buy INTEGER = 5;
		buyer_client INTEGER = 1;
		
		v_available_stock INTEGER;
		v_product_price INTEGER;
		v_user_exists INTEGER;
		v_factura_id INTEGER;
		
	BEGIN
		--Comprobar si hay existencias suficientes del producto.
		SELECT stock, price INTO v_available_stock, v_product_price
		FROM lyfter_transacciones.productos
		WHERE id = product_to_buy;
	
		IF v_available_stock IS NULL OR v_available_stock < quantity_to_buy THEN
			RAISE EXCEPTION 'Stock insuficiente. Abortando transacción.';
		END IF;

		--Confirmar que el usuario que realiza la compra existe en la DB.
		SELECT COUNT(*) INTO v_user_exists
		FROM lyfter_transacciones.usuarios
		WHERE id = buyer_client;

		IF v_user_exists = 0 THEN
			RAISE EXCEPTION 'Usuario no existe. Abortando transacción.';
		END IF;

		--Insertar la factura con el usuario relacionado.
		INSERT INTO lyfter_transacciones.facturas (usuarios_id, total) VALUES (buyer_client, (quantity_to_buy*v_product_price))
		RETURNING id INTO v_factura_id;
	
		INSERT INTO lyfter_transacciones.factura_items (facturas_id, producto_id, quantity, price)
        VALUES (v_factura_id, product_to_buy, quantity_to_buy, v_product_price);
	
		--Reducir el stock del producto según la cantidad comprada.
		UPDATE lyfter_transacciones.productos
		SET stock = stock - quantity_to_buy
		WHERE id = product_to_buy;

		RAISE NOTICE 'Transacción de Compra completada.';
			
END $$;