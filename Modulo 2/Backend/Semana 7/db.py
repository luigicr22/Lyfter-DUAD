import psycopg2

class PgManager:
    def __init__ (self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = self.create_connection(db_name, user, password, host, port)

    def create_connection (self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname = db_name, 
                user = user,
                password = password,
                host = host,
                port = port,
            )
            print("Conexion Creada")
            return connection
        except Exception as error:
            raise Exception ("Error al conectar a la base de datos")
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
        print("Conexion cerrada")
    
    def execute_query(self, query, *args):
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, *args)
                    print("Query Ejecutado")

                    if cursor.description:
                        results = cursor.fetchall()
                        return results
                    return True
        
        except psycopg2.Error as error:
            if error.pgcode == "23505":
                raise Exception ("Error: Valores de email o username incorrectos")
            
            if error.pgcode == "23514":
                raise Exception ("Error: Insertar un estado correcto")
            
            if error.pgcode == "22008":
                raise Exception ("Error: Formato de fecha incorrecto")
            
            if error.pgcode.startswith("P"):
                raise Exception (error.diag.message_primary)
            
            else:
                raise Exception ("Error en la conexion: ", error)