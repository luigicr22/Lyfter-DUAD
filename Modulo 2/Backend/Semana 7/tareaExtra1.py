from db import PgManager
from repositoryUser import UserRepository
from repositoryCar import CarsRepository
from repositoryRental import RentalRepository
import csv
from datetime import date
import os

def check_path(func):
    def wrapper (user,*args):
        if not os.path.exists("db_backups"):
            os.makedirs("db_backups")
        func(user,*args)
    return wrapper
    
@check_path
def create_csv (path, data, headers):
    with open(path, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

def main():
    try:
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
        date_today = date.today()

        #Creacion de backup Users
        users =  users_repo.get_all()
        create_csv (f"./db_backups/users_{date_today}.csv", users, users[0].keys())
        print ("Archivo Backup Users Creado")

        #Creacion de backup Cars
        cars =  cars_repo.get_all()
        create_csv (f"./db_backups/cars_{date_today}.csv", cars, cars[0].keys())
        print ("Archivo Backup Cars Creado")

        #Creacion de backup Rentals
        rentals =  rentals_repo.get_all()
        create_csv (f"./db_backups/rentals_{date_today}.csv", rentals, rentals[0].keys())
        print ("Archivo Backup Rentals Creado")

        db_manager.close_connection()

    except Exception as error:
        print (error)

if __name__ == "__main__":
    main()