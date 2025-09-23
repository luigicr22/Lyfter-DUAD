from datetime import datetime

class Math:
    
    def validate_numbers(func):
        def wrapper(cls, a, b):
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                print("Ambos argumentos deben ser números.")
            else:
                func(cls, a, b)
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