class Person:

    def __init__(self, name):
        self.name = name
    
    def check_args(func):
        def wrapper(self, age, height):
            print(f"El argumento ingresado para la edad es: {age}")
            print(f"El argumento ingresado para el altura es: {height}")
            if (isinstance(age, (int)) and isinstance(height, (float))):
                print (f"Se agregó los datos a la persona {func(self, age, height)}")
            else:
                print ("Los parámetros deben ser números")
        return wrapper

    @check_args
    def add_age_height(self, age, height):
        self.age = age
        self.height = height
        return self.name
    
luis = Person("Luis")
luis.add_age_height(38,1.72)
print("\n")
Ana = Person("Ana")
luis.add_age_height(38,"Un metro y medio")