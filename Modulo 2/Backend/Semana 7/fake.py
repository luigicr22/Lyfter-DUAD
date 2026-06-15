import random
from faker import Faker
from faker.providers import DynamicProvider
import faker.exceptions

# Seed script con Faker (Ejercicio Extra 3)

def insert_user(db_manager,quantity):
    fake = Faker()
    status_user_provider = DynamicProvider (
        provider_name= "status_user",
        elements=['Activo', 'Inactivo', 'Moroso']
        )
    fake.add_provider(status_user_provider)
    for n in range(quantity):
        db_manager.execute_query(f"INSERT INTO lyfter_car_rental.users (name, email, username, birthday, status, password) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;", 
            (fake.name(),fake.unique.email(),fake.unique.user_name(),fake.date_between(start_date='-80y', end_date='-18y'),fake.status_user(),fake.password(),))


def insert_car(db_manager,quantity):
    car_data = [
    {'manufacturer': 'Toyota', 'models': ['Corolla', 'Camry', 'RAV4', 'Hilux', 'Yaris', 'Prius', 'Tacoma', 'Land Cruiser', 'Highlander', 'Supra']},
    {'manufacturer': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang', 'Explorer', 'Escape', 'Edge', 'F-150', 'Bronco', 'Ranger', 'Fusion']},
    {'manufacturer': 'Chevrolet', 'models': ['Spark', 'Malibu', 'Impala', 'Cruze', 'Camaro', 'Tahoe', 'Suburban', 'Silverado', 'Blazer', 'Equinox']},
    {'manufacturer': 'Honda', 'models': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit', 'Odyssey', 'HR-V', 'Ridgeline', 'Passport', 'Insight']},
    {'manufacturer': 'BMW', 'models': ['X1', 'X3', 'X5', 'X7', '3 Series', '5 Series', '7 Series', 'M3', 'M4', 'Z4']},
    {'manufacturer': 'Mercedes-Benz', 'models': ['A-Class', 'C-Class', 'E-Class', 'S-Class', 'GLA', 'GLC', 'GLE', 'GLS', 'AMG GT', 'CLA']},
    {'manufacturer': 'Audi', 'models': ['A3', 'A4', 'A6', 'A8', 'Q3', 'Q5', 'Q7', 'Q8', 'RS6', 'TT']},
    {'manufacturer': 'Volkswagen', 'models': ['Golf', 'Jetta', 'Passat', 'Tiguan', 'Atlas', 'Arteon', 'ID.4', 'Touareg', 'Beetle', 'Polo']},
    {'manufacturer': 'Hyundai', 'models': ['Accent', 'Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Kona', 'Palisade', 'Veloster', 'Ioniq', 'Creta']},
    {'manufacturer': 'Nissan', 'models': ['Versa', 'Sentra', 'Altima', 'Maxima', 'Rogue', 'Murano', 'Pathfinder', 'Armada', '370Z', 'GT-R']}
    ]

    fake = Faker()
    status_car_provider = DynamicProvider (
        provider_name= "status_car",
        elements=['Disponible', 'Deshabilitado']
        )
    fake.add_provider(status_car_provider)

    #En esta parte utilizo una lista base de Manufacturer y Model para escoger los datos.
    #La idea era darle datos reales de una forma sencilla y a la vez que fueran random.
    #Como se tenia que escoger el modelo basado en el manufacturer, resolverlo con providers era mas extenso.

    for n in range(quantity):
        car_manufacturer = random.choice(car_data)
        car_model = random.choice(car_manufacturer['models'])
        db_manager.execute_query(f"INSERT INTO lyfter_car_rental.cars (manufacturer, model, year, status) VALUES (%s, %s, %s, %s);", 
            (car_manufacturer.get('manufacturer'),car_model,fake.date_this_decade().year,fake.status_car(),))


def insert_rental(db_manager,quantity):
    fake = Faker()

    users = db_manager.execute_query("SELECT id FROM lyfter_car_rental.users;")
    users_list =[]
    for user in users:
        users_list.append(user[0])

    cars = db_manager.execute_query("SELECT id FROM lyfter_car_rental.cars WHERE status = 'Disponible';")
    cars_list =[]
    for car in cars:
        cars_list.append(car[0])
    
    cars_provider = DynamicProvider (
        provider_name= "cars_rental",
        elements = cars_list
        )
    fake.add_provider(cars_provider)

    users_provider = DynamicProvider (
        provider_name= "users_rental",
        elements = users_list
        )
    fake.add_provider(users_provider)

    status_rental_provider = DynamicProvider (
        provider_name= "status_rental",
        elements = ['Activo','Completado']
        )
    fake.add_provider(status_rental_provider)

    for n in range(quantity):
        try:
            car_id = fake.unique.cars_rental()
            user_id = fake.users_rental()
            status = fake.status_rental()
            db_manager.execute_query(f"INSERT INTO lyfter_car_rental.rentals (car_id, user_id, status) VALUES (%s, %s, %s);",
                (car_id,user_id,status,))
            
            # Actualizo el status del carro en la tabla Cars si el alquiler esta en Curso.
            if status == 'Activo':
                db_manager.execute_query(f"UPDATE lyfter_car_rental.cars SET status = 'Alquilado' WHERE id = %s;",(car_id,))
        except faker.exceptions.UniquenessException:
            print ("Exceso de intentos sin valores repetidos")