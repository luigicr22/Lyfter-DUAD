#Ejercicio 3.3
#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

first_number = int(input("Ingresar el primer número: "))
second_number = int(input("Ingresar el segundo número: "))
third_number = int(input("Ingresar el tercero número: "))

if (first_number+second_number+third_number == 30 or first_number == 30 or second_number == 30 or third_number == 30):
    print("Es Correcto")
else:
    print("Es Incorrecto")

    