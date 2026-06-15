from db import PgManager

def main():
    try:
        db_manager = PgManager(
            db_name="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432
        )

        schema = 'lyfter_car_rental'
        tables = ['cars','users', 'rentals']

        for table in tables:
            exists = db_manager.execute_query("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = %s AND table_name = %s);",[schema, table])
            if exists[0][0]:
                print (f"Tabla {table} existe")
            else: 
                print (f"Tabla {table} no existe")
        
        count = db_manager.execute_query("SELECT COUNT(*) FROM lyfter_car_rental.cars;")
        if count[0][0] >= 1:
            print ("DB OK. Sistema operativo con normalidad")
        else: 
            print ("DB ERROR. No hay autos disponibles")

        db_manager.close_connection()

    except Exception as error:
        print (error)

if __name__ == "__main__":
    main()