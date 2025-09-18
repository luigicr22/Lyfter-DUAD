import csv
import os

def export_data(students):
    student_headers = ("full_name","section","Español","Inglés","Historia","Ciencias","average_grade")
    try:
        with open ('students.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,student_headers)
            writer.writeheader()
            for index1 in range(len(students)):
                student_row = {}
                student_row["full_name"]=students[index1]["full_name"]
                student_row["section"]=students[index1]["section"]
                for index2 in range(len(students[index1]["grades"])):
                    student_row[students[index1]["grades"][index2]["subject"]] = students[index1]["grades"][index2]["grade"]
                student_row["average_grade"]=students[index1]["average_grade"]
                writer.writerow(student_row)
        input(f"""Información exportada con éxito. 
Ubicacion del archivo:
{os.getcwd()}\students.csv
Presione cualquier tecla para continuar...""")
        return
    except FileNotFoundError:
        input("No se encuentra el path especificado. Presione cualquier tecla para continuar...")
        return


def import_data():
    students = []
    try:
        with open ('students.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for student_row in reader:
                student = {}

                student["full_name"]=student_row["full_name"]

                student["section"]=student_row["section"]

                grades_list = []
                grade_subject = {}
                subjects = ["Español", "Inglés","Historia","Ciencias"]
                for index in range(len(subjects)):
                    grade_subject ["subject"] = subjects[index]
                    grade_subject ["grade"] = student_row[subjects[index]]
                    grades_list.append(grade_subject.copy())
                student["grades"]=grades_list

                student["average_grade"]=student_row["average_grade"]

                students.append(student)
        input("Información importada con éxito. Presione cualquier tecla para continuar...")
        return students
    except FileNotFoundError:
        input(f"""No se encuentra el archivo students.csv en la carpeta:
{os.getcwd()}
Presione cualquier tecla para continuar...""")
        return students
    