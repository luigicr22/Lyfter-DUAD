from feature import utils
from objects import Student
import os

def add_students(students):
    os.system('cls')
    while True:
        while True:
            full_name = input("Ingrese el nombre completo del estudiante: ").title().strip()
            if utils.is_valid_name(full_name):
                break
        
        while True:
            section = input("Ingrese la sección del estudiante (Ejemplo: 11-B): ").upper().strip()
            if utils.is_valid_section(section):
                break
            
        if utils.exist_student(full_name, section, students):
            other_student = input("Presione \"N\" si desea finalizar de ingresar estudiantes, u otra tecla para continuar: ")
            if other_student == "N":
                return students
            else:
                continue
            
        subjects = ['Español', 'Inglés', 'Historia', 'Ciencias']
        grades = []
        for subject in subjects:
            grades.append(utils.input_grade(subject))
        
        average_grade = utils.calculate_average(grades)

        student = Student(full_name, section, grades, average_grade)
        students.append(student)

        other_student = input("Presione \"N\" si desea finalizar de ingresar estudiantes, u otra tecla para continuar: ")
        if other_student == "N":
            break
    return students


def remove_student(students):
    os.system('cls')
    
    while True:
        full_name = input("Ingrese el nombre completo del estudiante a eliminar: ").title().strip()
        if utils.is_valid_name(full_name):
            break
    
    while True:
        section = input("Ingrese la sección del estudiante (Ejemplo: 11-B): ").upper().strip()
        if utils.is_valid_section(section):
            break
        
    students = utils.exist_remove(full_name, section, students)
    return students


def view_students(students):
    os.system('cls')
    for student in students:
        print(f"Estudiante: {student.full_name}")
        print(f"   Sección: {student.section}")
        print(f"   Notas:")
        for index in range(len(student.grades)):
            print(f"\t{student.grades[index]['subject']}: {student.grades[index]['grade']}")
        print(f"   Nota promedio: {student.average_grade}\n")

    input("Presione Enter para continuar...")


def view_average_grades(students):
    os.system('cls')
    total_average = 0
    for student in students:
        total_average += student.average_grade
    total_average /= len(students)
    print(f"La nota promedio de los estudiantes (cantidad = {len(students)}) es de: {total_average:.2f}")
    input("Presione Enter para continuar...")


def view_failed_students(students):
    os.system('cls')
    print("Los estudiantes reprueban con una nota menor a 65\nLos estudiantes reprobados son:\n")
    failed_list = []
    for student in students:
        failed_student = {}
        for index in range(len(student.grades)):
            if student.grades[index]['grade'] < 65:
                failed_student["full_name"] = student.full_name
                failed_student["section"] = student.section
                failed_student["subject"] = student.grades[index]['subject']
                failed_student["grade"] = student.grades[index]['grade']
                failed_list.append(failed_student.copy())
    
    for student in failed_list:
        print(f"Estudiante: {student['full_name']}")
        print(f"   Sección: {student['section']}")
        print(f"   Materia: {student['subject']}")
        print(f"   Nota: {student['grade']}\n")
    
    input("Presione Enter para continuar...")


def view_top_students(students):
    os.system('cls')
    top_students = [{"full_name":"","average_grade":0},{"full_name":"","average_grade":0},{"full_name":"","average_grade":0}]
    for student in students:
        for index in range(3):
            if student.average_grade >= top_students[index]['average_grade']:
                top_students.insert(index,{'full_name':student.full_name,'average_grade':student.average_grade})
                top_students.pop(3)
                break
    
    position = 1
    print("Top 3 de estudiantes\n")
    for student in top_students:
        print(f"{position}° Estudiante: {student['full_name']}")
        print(f"   Nota: {student['average_grade']}\n")
        position += 1
    input("Presione Enter para continuar...")
