class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self._allowed_filters = ["id", "car_id", "user_id", "status", "rental_date"]
    
    
    def _format_rental(self, rental_record):
        return {
            'id':  rental_record[0],
            'car_id': rental_record[1],
            'user_id': rental_record[2],
            'status': rental_record[3],
            'rental_date': rental_record[4].isoformat()
            }
    
    #Crea una renta de automovil. Si el automovil tiene rentas activas o el usuario se encuentra 'Inactivo' o 'Moroso', no deja realizar el alquiler.
    def create(self, parameters):
        try:
            values = []
            for index in range(1,3):
                values.append(parameters[self._allowed_filters[index]])
                parameters.pop(self._allowed_filters[index])

            if parameters:
                raise KeyError
            
            self.db_manager.execute_query(f"""
                DO $$
                    DECLARE 
                        status_car character varying(20);
                        status_user character varying(20);
                        car_id INTEGER := %s;
                        user_id INTEGER := %s;
                        
                    BEGIN
                        SET search_path TO lyfter_car_rental;
                        
                        SELECT status INTO status_car
                        FROM cars
                        WHERE id = car_id;
                        
                        IF status_car = 'Alquilado' OR status_car = 'Deshabilitado' THEN
                            RAISE EXCEPTION 'Error: Carro no disponible' USING ERRCODE = 'P0001';
                        END IF;

                        SELECT status INTO status_user
                        FROM users
                        WHERE id = user_id;
                        
                        IF status_user = 'Moroso' OR status_user = 'Inactivo' THEN
                            RAISE EXCEPTION 'Error: Usuario no habilitado' USING ERRCODE = 'P0001';
                        END IF;

                        UPDATE cars SET status = 'Alquilado' WHERE id = car_id;
                        INSERT INTO rentals (car_id, user_id) values (car_id, user_id);
                        
                END $$;
                """,values,)
            return True     
         
        except KeyError:
            raise Exception ("Parametros faltante, sobrante o invalido")
        
        except Exception as error:
            raise Exception (error)

    
    #Modifica estado del alquiler, verificando estados de automoviles y alquileres antes.
    def update_status(self, id, status):
        try:
            self.db_manager.execute_query(f"""
                DO $$
                    DECLARE 
                        id_car INTEGER;
                        status_car character varying(20);
                        actual_status character varying(20);
                        id_rental INTEGER := %s;
                        new_status character varying(20) := %s;
                        
                    BEGIN
                        SET search_path TO lyfter_car_rental;
                        
                        SELECT status, car_id INTO actual_status, id_car
                        FROM rentals
                        WHERE id = id_rental;
                        
                        IF actual_status = new_status THEN
                            RAISE EXCEPTION 'Error: El alquiler se encuentra en el estado solicitado.' USING ERRCODE = 'P0005';
                        END IF;

                        IF actual_status = 'Completado' AND new_status = 'Activo' THEN
                            SELECT status INTO status_car
                            FROM cars
                            WHERE id = id_car;

                            IF status_car IN ('Alquilado', 'Deshabilitado') THEN
                                RAISE EXCEPTION 'Error: El automovil no esta disponible para reanudar el alquiler' USING ERRCODE = 'P0006';
                            END IF;

                            UPDATE cars SET status = 'Alquilado' WHERE id = id_car;		
                            UPDATE rentals SET status = new_status WHERE id = id_rental;
                        END IF;

                        IF actual_status = 'Activo' AND new_status = 'Completado' THEN
                            UPDATE cars SET status = 'Disponible' WHERE id = id_car;		
                            UPDATE rentals SET status = 'Completado' WHERE id = id_rental;
                        END IF;				
                END $$;
                """,(id, status),)
            return True
        
        except Exception as error:
            raise Exception (error)
    
    
    def delete(self, id):
        try:
            self.db_manager.execute_query(
                f"DELETE FROM lyfter_car_rental.rentals WHERE id = %s;",
                (id,),
            )
            return True
        
        except Exception as error:
            raise Exception (error)
    
    def get_all(self,parameters = {}):
        try:
            query = "SELECT * FROM lyfter_car_rental.rentals"
            filters = []
            values = []

            if parameters:
                for filter, value in parameters.items():
                    if filter in self._allowed_filters:
                        filters.append(f"{filter} = %s")
                        values.append(value)
                    else:
                        raise Exception ("Parametro invalido")

                if filters:
                    query += " WHERE " + " AND ".join(filters)

            query += " ORDER BY id ASC"
            results = self.db_manager.execute_query(query,values)
            formatted_result = [self._format_rental(result) for result in results]
            return formatted_result
        
        except Exception as error:
            raise Exception (error)
    
    
