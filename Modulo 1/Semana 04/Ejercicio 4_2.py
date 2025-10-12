#Ejercicio 4.2
#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if (age>=65):
    stage = "adulto mayor"
elif (age>35):
    stage = "adulto"
elif (age>=18):
    stage = "adulto joven"
elif (age>=15):
    stage = "adolescente"
elif (age>=12):
    stage = "preadolescente"
elif (age>=2):
    stage = "niño"
else:
    stage = "bebé"

print(f"{name} {lastname}, usted es un {stage}")