#Ejercicio 2.2
#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

time = int(input("Ingrese una cantidad de segundos: "))

if (time < 600):
    print(f"Los segundos faltantes para llegar a 10min son: {600-time}")
elif (time == 600):
    print("Los segundos ingresados son igual a 10min")
else:
    print("Los segundos ingresados son mayores a 10min")