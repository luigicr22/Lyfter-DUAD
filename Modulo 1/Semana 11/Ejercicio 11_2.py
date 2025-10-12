class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print (f"Ha nacido una nueva persona!: {name}")
    

class Bus():
    passengers = []

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        print(f"Se ha creado un bus de {max_passengers} pasajeros")
    
    def add_passenger(self,passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} se ha montado al bus")
        else:
            print(f"{passenger.name} no se pudo montar al bus. El bus ya esta lleno")

    def pop_passenger(self,number_passenger):
        if number_passenger <= len(self.passengers): 
            passenger = self.passengers.pop(number_passenger-1)
            print(f"{passenger.name} a sido bajad@ del bus")
        else:
            print(f"El bus solo tiene {len(self.passengers)} pasajeros, numero invalido")

bus = Bus(2)
person1 = Person("Luis",38)
person2 = Person("Ana",40)
person3 = Person("Irene",35)

bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)

bus.pop_passenger(3)
bus.pop_passenger(2)
