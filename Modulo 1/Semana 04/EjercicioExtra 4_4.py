#Ejercicios Extra 4.
#Tabla de multiplicar personalizada
#   Pida al usuario un número del 1 al 10
#   Muestre su tabla de multiplicar del 1 al 12

number = int(input("Ingrese un número del 1 al 10: "))
print(f"La tabla de multiplicar del {number} es:")

for count in range(12):
    print(f"{number}x{(count+1)}={number*(count+1)}")