#Ejercicio Extra 3.3
#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.

highest_number = 0
for count in range(100):
    number = int(input("Ingrese un número: "))
    if (number > highest_number):
        highest_number = number

print(f"El número mayor es: {highest_number}")