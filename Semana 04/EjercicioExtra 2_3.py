#Ejercicio Extra 2.3
#Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

total_women = 0
total_men = 0
count = 0

while (count < 6):
    sex = int(input(f"""Ingresando 1 si es mujer o 2 si es hombre
    Ingrese el sexo de la persona #{count+1}: """))

    if (sex == 1):
        total_women += 1
        count += 1        
    elif (sex == 2):
        total_men += 1
        count += 1
    else:
        print("Ingrese 1 0 2 solamente")

percentage_men = total_men * 100 / (count)
percentage_women = total_women * 100 / (count)

print(f"""El porcentaje de mujeres es: {percentage_women}
El porcentaje de hombres es: {percentage_men}""")