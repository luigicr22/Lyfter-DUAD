def function_sum (number1,number2):
    sum = number1 + number2
    return sum


def function_average (list_numbers):
    average = 0
    for number in list_numbers:
        average += number
    len_list = len(list_numbers) - list_numbers.count(0)
    average = int(average / len_list)
    return average


def function_modulus(number1,number2):
    if number2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return number1 % number2
