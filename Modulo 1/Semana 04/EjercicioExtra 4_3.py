#Ejercicios Extra 3.
#Convertidor de unidades de temperatura
# - Pida al usuario ingresar una temperatura en Celsius
# - Conviértala a Fahrenheit y Kelvin
# - Muestre los tres valores

celsius = float(input("Ingrese temperatura en Celsius: "))

print(f"Temperatura en celsius: {celsius}")
print(f"Temperatura en fahrenheit: {(celsius * 1.8) + 32}")
print(f"Temperatura en kelvin: {celsius + 273.5}")