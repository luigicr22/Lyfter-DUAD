class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self._allowed_filters = ["id", "name", "email", "username", "birthday", "password", "status"]
    
    
    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "email": user_record[2],
            "username": user_record[3],
            "birthday": user_record[4].isoformat(),
            "status": user_record[5],
            "password": user_record[6],
            }
    
    # Crea usuario, la DB verifica email existente, username existente.
    # El estado se crea por default 'Activo'
    def create(self, parameters):
        try:
            values = []

            for index in range(1,6):
                values.append(parameters[self._allowed_filters[index]])
                parameters.pop(self._allowed_filters[index])

            if parameters:
                raise KeyError

            self.db_manager.execute_query(f"INSERT INTO lyfter_car_rental.users (name, email, username, birthday, password) VALUES (%s, %s, %s, %s, %s);",
                (values))
            return True
        
        except KeyError:
            raise Exception ("Parametros faltante, sobrante o invalido")
        
        except Exception as error:
            raise Exception (error)
    
    
    #Cambia es estado del usuario. Si tiene rentas activas no permite cambiar el estado a 'Inactivo'
    def update_status(self, id, status):
        try:
            self.db_manager.execute_query(f"""
                DO $$
                    DECLARE 
                        active_rents INTEGER;
                        id_user INTEGER := %s;
                        status_user character varying(20) := %s;
                        
                    BEGIN
                        SET search_path TO lyfter_car_rental;
                        
                        IF status_user = 'Inactivo' THEN
                            SELECT id INTO active_rents
                            FROM rentals
                            WHERE user_id = id_user AND status = 'Activo'
                            LIMIT 1;
                            
                            IF active_rents IS NOT NULL THEN			
                                RAISE EXCEPTION 'Error: El usuario tiene rentas activas.' USING ERRCODE = 'P0002';
                            END IF;
                        END IF;
                        
                        UPDATE users SET status = status_user WHERE id = id_user;
                    
                END $$;
                """, (id,status),)
            return True
        
        except Exception as error:
            raise Exception (error)
    
    
    def delete(self, id):
        try:
            self.db_manager.execute_query(
                f"DELETE FROM lyfter_car_rental.users WHERE id = %s;",
                (id,),)
            return True
        
        except Exception as error:
            raise Exception (error)
    
    def get_all(self,parameters = {}):
        try:
            query = "SELECT * FROM lyfter_car_rental.users"
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
            formatted_result = [self._format_user(result) for result in results]
            return formatted_result
        
        except Exception as error:
            raise Exception (error)