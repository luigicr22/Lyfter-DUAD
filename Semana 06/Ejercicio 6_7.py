def is_prime (number):
#El algoritmo consiste en los siguientes pasos a seguir:
#Primero verificar si es divisible con 2,3 y 5. Si es divisible entonces es compuesto.
#Segundo hallar la raíz cuadrada del número, si la raíz es exacta entonces el número es compuesto.
#Si la raíz es inexacta, entonces se prueba si es divisible con todos los números primos menores que la raíz obtenida, excepto 2, 3 y 5.
#Si es divisible con algún número primo entonces es compuesto, en caso contrario es primo.
    if number == 1 or number == 0:
        is_prime = False
    elif number == 2 or number == 3 or number == 5:
        is_prime = True
    elif number%2 == 0 or number%3 == 0 or number%5 == 0:
        is_prime = False
    elif ((number**(1/2))%1) == 0:
        is_prime = False
    else:
        is_prime = True
        for index in range(3,int((number**(1/2))+1)):
            if number%(index) == 0:
                is_prime = False
                break
    return (is_prime)


def check_list (list_to_check):
    list_prime = []
    for number in list_to_check:
        if is_prime(number):
            list_prime.append(number)
    return (list_prime)


def main ():
    original_list = [1, 4, 6, 7, 13, 9, 67]
    print(check_list(original_list))


if __name__ == "__main__":
    main()