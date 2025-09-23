class Person:

    def __init__(self, name):
        self.name = name
    
    def show_arg(func):
        def wrapper(self, age, country):
            print(f"El argumento ingresado para la edad es: {age}")
            print(f"El argumento ingresado para el pais es: {country}")
            print (f"Se agregó los datos a la persona {func(self, age, country)}")
        return wrapper

    @show_arg
    def add_age_country(self, age, country):
        self.age = age
        self.country = country
        return self.name
    
luis = Person("Luis")
luis.add_age_country(38,"Costa Rica")