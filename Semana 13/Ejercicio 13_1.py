class Person:

    def __init__(self, name):
        self.name = name
    
    def show_arg(func):
        def wrapper(self, age, **kwargs):
            if isinstance(age,int):
                print(f"El argumento ingresado para la edad es: {age}")
                print(f"Otros parametro ingresados: {kwargs}")
                func(self, age, **kwargs)
            else:
                print(f"El argumento para edad, \"{age}\", no es un número")
                return
        return wrapper

    @show_arg
    def add_age_country(self, age, **kwargs):
        self.age = age
        self.additional_info = kwargs
        return print(f"Se agregó los datos a {self.name}")
    
luis = Person("Luis")
luis.add_age_country(38,pais="Costa Rica", ciudad="San Jose")
print("\n")
ana = Person("Ana")
ana.add_age_country("veinte",pais="Costa Rica", ciudad="San Jose")