DO $$
	DECLARE
		products_to_buy INTEGER [] = ARRAY[1,2,3];
		quantities_to_buy INTEGER [] = ARRAY[5,6,8];
		timestamps_to_buy timestamp [];
		prices_to_buy INTEGER [];
		buyer_client INTEGER = 1;

		v_user_exists INTEGER;
		v_index INTEGER;
		v_available_stock INTEGER;
		v_product_price INTEGER;
		v_factura_total INTEGER = 0;
		v_timestamp timestamp;
		v_factura_id INTEGER;
		v_update_ok INTEGER;

	BEGIN
		SELECT COUNT(*) INTO v_user_exists
		FROM lyfter_transacciones.usuarios
		WHERE id = buyer_client;

		IF v_user_exists = 0 THEN
			RAISE EXCEPTION 'Usuario no existe. Abortando transacción.';
		END IF;

		FOR v_index IN 1 .. array_length(products_to_buy, 1) LOOP
			SELECT stock, price INTO v_available_stock, v_product_price
			FROM lyfter_transacciones.productos
			WHERE id = products_to_buy[v_index];

			IF v_available_stock < quantities_to_buy[v_index] THEN
				RAISE EXCEPTION 'Uno de los productos no tiene suficiente en existencia. Abortando transacción.';
			END IF;

			v_timestamp = CURRENT_TIMESTAMP;
			UPDATE lyfter_transacciones.productos
			SET timestamp_stock = v_timestamp
			WHERE id = products_to_buy[v_index];
			
			v_factura_total = v_factura_total + (quantities_to_buy[v_index] * v_product_price);
			prices_to_buy = array_append(prices_to_buy, v_product_price);
			timestamps_to_buy = array_append(timestamps_to_buy, v_timestamp);

		END LOOP;

		BEGIN
			INSERT INTO lyfter_transacciones.facturas (usuarios_id, total) VALUES (buyer_client, v_factura_total)
			RETURNING id INTO v_factura_id;
	
			FOR v_index IN 1 .. array_length(products_to_buy, 1) LOOP
				INSERT INTO lyfter_transacciones.factura_items (facturas_id, producto_id, quantity, price)
				VALUES (v_factura_id, products_to_buy[v_index], quantities_to_buy[v_index], prices_to_buy[v_index]);
			END LOOP;
			
			FOR v_index IN 1 .. array_length(products_to_buy, 1) LOOP		
				UPDATE lyfter_transacciones.productos
				SET stock = stock - quantities_to_buy[v_index]
				WHERE id = products_to_buy[v_index]
					AND timestamp_stock = timestamps_to_buy[v_index];

				GET DIAGNOSTICS v_update_ok = ROW_COUNT;

				IF v_update_ok = 0 THEN
					RAISE EXCEPTION 'Conflicto de concurrencia';
				END IF;
			END LOOP;

			EXCEPTION
        		WHEN OTHERS THEN
					RAISE EXCEPTION 'El stock cambió mientras se procesaba. Abortando transacción.';
			END;
			
		RAISE NOTICE 'Transacción de Compra finalizada.';
END $$;