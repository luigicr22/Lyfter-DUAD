class Person:

    def __init__(self, name):
        self.name = name
    
    def check_args(func):
        def wrapper(self, *args):
            all_numbers = True
            for index, arg in enumerate(args):
                if not isinstance(arg, (int,float)):
                    all_numbers = False
            if all_numbers:
                print (f"Se agregó los datos a la persona {func(self, *args)}")
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