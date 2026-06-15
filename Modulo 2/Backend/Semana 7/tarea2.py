from db import PgManager
from repositoryUser import UserRepository
from repositoryCar import CarsRepository
from repositoryRental import RentalRepository

def main():
    db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )

    users_repo = UserRepository(db_manager)
    cars_repo = CarsRepository(db_manager)
    rentals_repo = RentalRepository(db_manager)

    #EJERCICIO 1
    #Un script que agregue un usuario nuevo
    #El repository esta pensado para crear el nuevo usuario con el estado por defecto 'Activo'
    try:
        parameters = {"name":"Ryan Washington","email":"tkidd2@example.com","username":"ppeters2","birthday":"1983-12-27","password":"mvHHFS2V%7"}
        print(users_repo.create(parameters))
    except Exception as error:
        print(error)

    #Probando el error de email o usuario ya existente.
    try:
        print(users_repo.create(parameters))
    except Exception as error:
        print(error)  

    #EJERCICIO 2
    #Un script que agregue un automovil nuevo
    #El repository esta pensado para crear el nuevo automovil con el estado por defecto 'Disponible'
    try:
        parameters = {"manufacturer":"BMW", "model":"X5", "year":"2026"}
        print(cars_repo.create(parameters))
    except Exception as error:
        print(error)

    
    #EJERCICIO 3
    #Un script que cambie el estado de un usuario
    try:
        print(users_repo.update_status(1,'Activo'))
    except Exception as error:
        print(error)

    #Probando que si el usuario tiene rentas activas, no deja pasarlo a inactivo
    try:
        print(users_repo.update_status(10,'Inactivo'))
    except Exception as error:
        print(error)

    #Probando el error con un estado no valido.
    try:
        print(users_repo.update_status(1,'Pensativo'))
    except Exception as error:
        print(error)

    
    #EJERCICIO 4
    #Un script que cambie el estado de un automovil
    try:
        print(cars_repo.update_status(11,'Disponible'))
    except Exception as error:
        print(error)
    
    #Probando el error con un estado no valido.
    try:
        print(cars_repo.update_status(11,'En todas'))
    except Exception as error:
        print(error) 

    #Probando que si el automovil tiene rentas activas, no deja pasarlo a 'Disponible' o 'Deshabilitado'.
    try:
        print(cars_repo.update_status(4,'Deshabilitado'))
    except Exception as error:
        print(error) 

    #Probando que no se puede pasar a alquilado desde aqui, tiene que ser desde la modificacion del alquiler.
    try:
        print(cars_repo.update_status(4,'Alquilado'))
    except Exception as error:
        print(error) 
    

    #EJERCICIO 5
    #Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
    try:
        parameters = {"car_id": 3, "user_id": 5}
        print(rentals_repo.create(parameters))
    except Exception as error:
        print(error)

    #Probando que si el automovil tiene rentas activas o el usuario se encuentra 'Inactivo' o 'Moroso', no deja realizar el alquiler.
    try:
        parameters = {"car_id": 3, "user_id": 5}
        print(rentals_repo.create(parameters))
    except Exception as error:
        print(error)

        
    #EJERCICIO 6
     #Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler
    #
    try:
        print(rentals_repo.update_status(2,'Completado'))
    except Exception as error:
        print(error)
    
    #Probando que si el nuevo estado es el actual, no modifica nada.
    try:
        print(rentals_repo.update_status(2,'Completado'))
    except Exception as error:
        print(error)
    
    #Probando que si el nuevo estado es activo, verifica si el automovil asociado esta disponible antes de modificarlo.
    try:
        print(rentals_repo.update_status(4,'Activo'))
    except Exception as error:
        print(error)


    #EJERCICIO 7
    #Un script que deshabilite un automovil del alquiler
    try:
        print(cars_repo.update_status(4,'Deshabilitado'))
    except Exception as error:
        print(error)
        
    #Probando el error con un estado no valido.
    try:
        print(cars_repo.update_status(11,'Para Fuera'))
    except Exception as error:
        print(error) 

    #Probando que si el automovil tiene rentas activas, no deja pasarlo a 'Disponible' o 'Deshabilitado'.
    try:
        print(cars_repo.update_status(6,'Deshabilitado'))
    except Exception as error:
        print(error)

    #EJERCICIO 8
    #Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
    try:
        filters = {"status" : "Alquilado"}
        formatted_results = cars_repo.get_all(filters)
        print(formatted_results)
    except Exception as error:
        print(error)
    
    try:
        filters = {"status" : "Disponible"}
        formatted_results = cars_repo.get_all(filters)
        print(formatted_results)
    except Exception as error:
        print(error)

    db_manager.close_connection()

if __name__ == "__main__":
    main()