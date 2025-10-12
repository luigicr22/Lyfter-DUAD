#Ejercicio 4.5
#Dada `n` cantidad de notas de un estudiante, calcular:
#    1. Cuantas notas tiene aprobadas (mayor a 70).
#    2. Cuantas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.

grade_counter = 1
approved_grades = 0
unapproved_grades = 0
average_approved_grades = 0
average_unapproved_grades = 0
average_total_grades = 0

total_grades = int(input("Ingrese la cantidad de notas: "))

while (grade_counter <= total_grades):
    grade = int(input(f"Ingrese la nota numero {grade_counter}: "))
    if (grade < 70):
        unapproved_grades += 1
        average_unapproved_grades = average_unapproved_grades + grade
    else:
        approved_grades += 1
        average_approved_grades = average_approved_grades + grade

    average_total_grades = average_total_grades + (grade / total_grades)
    grade_counter += 1

print(f"El estudiante tiene esta cantidad de notas aprobadas: {approved_grades}")
if (approved_grades != 0):
    average_approved_grades = average_approved_grades / approved_grades
    print(f"Este es el promedio de notas aprobadas: {average_approved_grades}")

print(f"El estudiante tiene esta cantidad de notas desaprobadas: {unapproved_grades}")
if (unapproved_grades != 0):
    average_unapproved_grades = average_unapproved_grades / unapproved_grades
    print(f"Este es el promedio de notas desaprobadas: {average_unapproved_grades}")

print(f"Este es el promedio total de notas: {average_total_grades}")