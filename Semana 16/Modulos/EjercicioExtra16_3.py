def divide(number1, number2):
    if isinstance(number1,int) and isinstance(number2,int):
        if number2 == 0:
            raise ValueError("No se puede dividir por cero")
        return number1 / number2
    else:
        raise TypeError("No se aceptan strings")