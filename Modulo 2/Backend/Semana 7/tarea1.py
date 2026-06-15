from db import PgManager
from fake import insert_user, insert_car, insert_rental

def main():
    db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )
    
    #Cree un nuevo schema llamado lyfter_car_rental
    db_manager.execute_query("CREATE SCHEMA lyfter_car_rental AUTHORIZATION postgres;")
    
    #Cree un script donde se cree una tabla de usuarios
    db_manager.execute_query(
        """CREATE TABLE lyfter_car_rental.users(
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        name character varying(35) NOT NULL,
        email character varying(50) NOT NULL UNIQUE,
        username character varying(25) NOT NULL UNIQUE,
        birthday date NOT NULL,
        status character varying(20) NOT NULL DEFAULT 'Activo'
			CHECK (status IN ('Activo', 'Inactivo', 'Moroso')),
        password character varying(25),
        PRIMARY KEY (id)
        );"""
    )
    
    #Cree un script donde se cree una tabla de automóviles
    db_manager.execute_query(
        """CREATE TABLE lyfter_car_rental.cars(
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        manufacturer character varying(30) NOT NULL,
        model character varying(30) NOT NULL,
        year integer NOT NULL,
        status character varying(20) NOT NULL DEFAULT 'Disponible'
			CHECK (status IN ('Disponible', 'Alquilado', 'Deshabilitado')),
        PRIMARY KEY (id)
        );"""
    )
    
    #cree una tabla cruz para relacionar los alquileres de los carros con los usuarios
    db_manager.execute_query(
        """CREATE TABLE lyfter_car_rental.rentals(
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        car_id integer NOT NULL,
        user_id integer NOT NULL,
        status character varying(20) NOT NULL DEFAULT 'Activo'
			CHECK (status in ('Activo','Completado')), 
        rental_date timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        CONSTRAINT car_id FOREIGN KEY (car_id)
            REFERENCES lyfter_car_rental.cars (id),
        CONSTRAINT user_id FOREIGN KEY (user_id)
            REFERENCES lyfter_car_rental.users (id)
        );"""
    )

    #El script debe popular las tablas
    #Ejercicio Extra 3 - Seed script con Faker
    insert_user(db_manager,200)
    insert_car(db_manager,100)
    insert_rental(db_manager,50)

    db_manager.close_connection()

if __name__ == "__main__":
    main()