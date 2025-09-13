import os

#Funcion Sumar
def add_number (current_number):
    os.system("cls")
    print("OPERACION SUMAR")
    print(f"Valor actual: {current_number}")
    try:
        number_to_sum = float(input("Digite el número que desea sumar al valor actual: "))
        current_number += number_to_sum
        print(f"Resultado / Valor actual: {current_number}")
    except ValueError as ex:
        raise ex
    return current_number


#Funcion Restar
def subtract_number (current_number):
    os.system("cls")
    print("OPERACION RESTAR")
    print(f"Valor actual: {current_number}")
    try:
        number_to_sub = float(input("Digite el número que desea restar al valor actual: "))
        current_number -= number_to_sub
        print(f"Resultado / Valor actual: {current_number}")
    except ValueError as ex:
        raise ex
    return current_number


#Funcion Multiplicar
def multiply_number(current_number):
    os.system("cls")
    print("OPERACION MULTIPLICAR")
    print(f"Valor actual: {current_number}")
    try:
        number_to_multi = float(input("Digite el número que desea multiplicar al valor actual: "))
        current_number *= number_to_multi
        print(f"Resultado / Valor actual: {current_number}")
    except ValueError as ex:
        raise ex
    return current_number


#Funcion Dividir
def divide_number(current_number):
    os.system("cls")
    print("OPERACION DIVIDIR")
    print(f"Valor actual: {current_number}")
    try:
        number_to_div = float(input("Digite el número que desea dividir al valor actual: "))
        current_number /= number_to_div
        print(f"Resultado / Valor actual: {current_number}")
    except ValueError as ex:
        raise ex
    except ZeroDivisionError:
        os.system("cls")
        print("No se puede dividir entre 0")
        print(f"Valor actual: {current_number}")
    return current_number



#Funcion Main (Menu principal)
def main ():
    current_number = 0.0
    user_continue = True
    print(f"Valor actual: {current_number}")

    while user_continue:
        try:
                print(f"MENU PRINCIPAL\n\t1- Sumar\n\t2- Restar\n\t3- Multiplicar\n\t4- Dividir\n\t5- Limpiar Memoria\n\t0- Salir""")
                option_user = int(input("Digite una opción (0-5): "))
                if option_user == 0:
                    #Salir
                    user_continue = False
                elif option_user == 1:
                    #Funcion Sumar
                    current_number = add_number(current_number)
                elif option_user == 2:
                    #Funcion restar
                    current_number = subtract_number(current_number)
                elif option_user == 3:
                    #Funcion multiplicar
                    current_number = multiply_number(current_number)
                elif option_user == 4:
                    #Funcion dividir
                    current_number = divide_number(current_number)
                elif option_user == 5:
                    current_number = 0.0
                    os.system('cls')
                    print(f"Valor actual {current_number}")
                else:
                    raise Exception("Ingrese un número en el rango")
        
        except ValueError:
            os.system("cls")
            print("Ingrese un valor válido")
            print(f"Valor actual: {current_number}")

        except Exception as ex:
            os.system("cls")
            print(ex)


if __name__ == "__main__":
    main()