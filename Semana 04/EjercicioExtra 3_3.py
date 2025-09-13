#Ejercicio Extra 3.3
#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.

sum = 0
for count in range(100):
    sum += int(input("Ingrese un número: "))

print(f"La suma de todos los números es: {sum}")