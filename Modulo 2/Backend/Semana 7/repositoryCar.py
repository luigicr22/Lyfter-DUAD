class CarsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self._allowed_filters = ["id", "manufacturer", "model", "year", "status"]

    def _format_car(self, car_record):
        return {
            'id': car_record[0],
            'manufacturer': car_record[1],
            'model': car_record[2],
            'year': car_record[3],
            'status': car_record[4],
            }
    
    #Crea un automovil nuevo, y es creado con un estado por default 'Disponible'
    def create(self, parameters):
        try:
            values = []

            for index in range(1,4):
                values.append(parameters[self._allowed_filters[index]])
                parameters.pop(self._allowed_filters[index])

            if parameters:
                raise KeyError

            self.db_manager.execute_query(f"INSERT INTO lyfter_car_rental.cars (manufacturer, model, year) VALUES (%s, %s, %s);",
                (values))
            return True
        
        except KeyError:
            raise Exception ("Parametros faltante, sobrante o invalido")
        
        except Exception as error:
            raise Exception (error)
    
    
    #Actualiza el estado del automovil. Si tiene rentas activas no deja pasarlo a 'Disponible' o 'Deshabilitado'.
    def update_status(self, id, status):
        try:
            self.db_manager.execute_query(f"""
                DO $$
                    DECLARE 
                        active_rents INTEGER;
                        id_car INTEGER := %s;
                        status_car character varying(20) := %s;
                        
                    BEGIN
                        SET search_path TO lyfter_car_rental;
                        
                        IF status_car IN ('Disponible','Deshabilitado') THEN
                        
                            SELECT id INTO active_rents
                            FROM rentals
                            WHERE car_id = id_car AND status = 'Activo'
                            LIMIT 1;
                            
                            IF active_rents IS NOT NULL THEN			
                                RAISE EXCEPTION 'Error: El carro esta con una renta activa.' USING ERRCODE = 'P0003';
                            END IF;
                        END IF;
                        
                        IF status_car = 'Alquilado' THEN
                            RAISE EXCEPTION 'Error: No se puede modificar a estado alquilado sin modificar un alquiler asociado.' USING ERRCODE = 'P0004';
                        END IF;   
                        UPDATE cars SET status = status_car WHERE id = id_car;
                                
                END $$;                
                """,(id, status),)
            return True
        
        except Exception as error:
            raise Exception (error)
    
    
    def delete(self, id):
        try:
            self.db_manager.execute_query(
                f"DELETE FROM lyfter_car_rental.cars WHERE id = %s;",
                (id,),
            )
            return True
        
        except Exception as error:
            raise Exception (error)
    

    def get_all(self,parameters = {}):
        try:
            query = "SELECT * FROM lyfter_car_rental.cars"
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
            formatted_result = [self._format_car(result) for result in results]
            return formatted_result
        
        except Exception as error:
            raise Exception (error)