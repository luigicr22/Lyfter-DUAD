class Vehicle:

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
    
    def get_info(self):
        print(f"Marca del vehiculo: {self._brand}")
        print(f"Año del vehiculo: {self._year}")


class Car(Vehicle):
    
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors= doors
    
    def get_info(self):
        super().get_info()
        print(f"Puertas el vehiculo: {self._doors} puertas\n")

class Motorcycle(Vehicle):

    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type= type
    
    def get_info(self):
        super().get_info()
        print(f"Tipo de vehiculo: {self._type}\n")

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

vehicle1.get_info()
vehicle2.get_info()