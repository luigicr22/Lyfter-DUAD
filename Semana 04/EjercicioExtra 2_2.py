#Ejercicio Extra 2.2
#Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. 

speed_kmh = int(input("Ingrese una velocidad en Km/h: "))

speed_ms = speed_kmh * 1000 / 3600

print(f"La velocidad en m/s es: {speed_ms}")