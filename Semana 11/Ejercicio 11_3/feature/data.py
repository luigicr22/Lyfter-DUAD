import csv
import os
from objects import Student


def export_data(students):
    os.system('cls')
    student_headers = ("full_name","section","Español","Inglés","Historia","Ciencias","average_grade")
    try:
        with open ('students.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,student_headers)
            writer.writeheader()
            for student in students:
                student_row = {}
                student_row["full_name"]=student.full_name
                student_row["section"]=student.section
                for grade in student.grades:
                    student_row[grade["subject"]] = grade["grade"]
                student_row["average_grade"]=student.average_grade
                writer.writerow(student_row)
        input(f"""Información exportada con éxito. 
Ubicacion del archivo:
{os.getcwd()}\students.csv
Presione cualquier tecla para continuar...""")
        return
    except FileNotFoundError:
        input("No se encuentra el path especificado.\nPresione cualquier tecla para continuar...")
        return


def import_data():
    os.system('cls')
    students = []
    try:
        with open ('students.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for student_row in reader:

                full_name=student_row["full_name"]

                section=student_row["section"]

                grades = []
                grade_subject = {}
                subjects = ["Español", "Inglés","Historia","Ciencias"]
                for index in range(len(subjects)):
                    grade_subject ["subject"] = subjects[index]
                    grade_subject ["grade"] = int(student_row[subjects[index]])
                    grades.append(grade_subject.copy())
                
                average_grade=float(student_row["average_grade"])
                student = Student(full_name,section,grades,average_grade)
                students.append(student)
        input("Información importada con éxito.\nPresione cualquier tecla para continuar...")
        return students
    except FileNotFoundError:
        input(f"""No se encuentra el archivo students.csv en la carpeta:
{os.getcwd()}
Presione cualquier tecla para continuar...""")
        return False