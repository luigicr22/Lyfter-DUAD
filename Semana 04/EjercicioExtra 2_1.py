#Ejercicio Extra 2.1
#Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (primero y segundo) y los ordene de menor a mayor en dichas variables.

first_number = int(input("Ingrese el primer número: "))
second_number = int(input("Ingrese el segundo número: "))

if (first_number > second_number):
    temporary_number = first_number
    first_number = second_number
    second_number = temporary_number

print(f"""Los númeos ordenados son:
      #1: {first_number}
      #2: {second_number}""")