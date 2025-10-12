#Ejercicio 4.4
#Cree un programa que le pida tres números al usuario y muestre el mayor.

highest_number = 0
for count in range(3):
    number = int(input(f"Ingrese el {count+1}° número: "))
    if (number > highest_number):
        highest_number = number

print(f"El número mayor es el {highest_number}")