#Ejercicio Extra 3.2
#Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3, “Buzz” si es divisible entre 5, y “FizzBuzz” si es divisible entre ambos.

number = int(input("Ingrese un número: "))

result = ""

if (number%3 == 0):
    result += "Fizz"
if (number%5 == 0):
    result += "Buzz"

print(result)