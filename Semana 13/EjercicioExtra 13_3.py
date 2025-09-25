from datetime import datetime

class Math:
    
    def validate_numbers(func):
        def wrapper(cls, *args):
            all_numbers = True
            for index, arg in enumerate(args):
                if not isinstance(arg, (int,float)):
                    all_numbers = False
            if all_numbers:
                return (func(cls, *args))
            else:
                return print("Ambos argumentos deben ser números.")
            
        return wrapper
    
    def log_call(func):
        def wrapper(cls, a, b):
            print(f"Nombre de la función: {func.__name__}")
            print(f"Argumentos: {a}, {b}")
            print(f"Fecha actual: {datetime.now()}")
            print(f"Resultado = {func(cls, a, b)}")
        return wrapper
    
    @classmethod
    @validate_numbers 
    @log_call   
    def multiply(cls, a, b):
        return a * b    

Math.multiply(5, 3)
print("\n")
Math.multiply(5, 'a')