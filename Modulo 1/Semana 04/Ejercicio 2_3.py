#Ejercicio 2.3
#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.

count = 1
sum = 0

number = int(input("Ingrese un número: "))

while (count <= number):
    sum += count
    count += 1

print(f"La suma de los números es: {sum}")