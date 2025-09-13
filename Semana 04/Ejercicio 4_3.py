#Ejercicio 4.3
#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
secret_number = random.randint(1,10)
guessed = False

while (not guessed):
    user_number = int(input("Adivine el número secreto del 1 al 10. Ingrese un número: "))
    if (user_number==secret_number):
        guessed = True
    else:
        print("Número incorrecto")

print(f"Adivinaste. El número secreto era {secret_number}")