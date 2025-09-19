import os
from feature import actions
from feature import data


def start_menu ():
    students = []
    while True:
        os.system('cls')
        print("""
MENU PRINCIPAL
    1. Ingresar un nuevo estudiante
    2. Eliminar a un estudiante
    3. Ver la información de todos los estudiantes
    4. Ver el top 3 de los estudiantes con la mejor nota promedio
    5. Ver la nota promedio entre las notas de todos los estudiantes
    6. Mostrar estudiantes reprobados
    7. Importar los datos de un archivo CSV previamente exportado
    8. Exportar todos los datos actuales a un archivo CSV
    9. Salir
        """)
        try:
            option = int (input("Seleccione una opción: "))
            match option:
                case 1:
                    students = actions.add_students(students)
                case 2:
                    students = actions.remove_student(students)
                case 3:
                    actions.view_students(students)
                case 4:
                    actions.view_top_students(students)
                case 5:
                    actions.view_average_grades(students)
                case 6:
                    actions.view_failed_students(students)
                case 7:
                    students_imported = data.import_data()
                    if students_imported != False:
                        students = students_imported
                case 8:
                    data.export_data(students)
                case 9:
                    save_before = input("Presione \"S\" si desea exportar los datos antes de salir: ")
                    if save_before.upper() == 'S':
                        data.export_data(students)
                        exit()
                    else:
                        exit()
                case _:
                    print("Opción no válida. Intente de nuevo.")
                    input("Presione Enter para continuar...")
        except ValueError:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        
        except Exception as ex:
            print(f"Ocurrió un error: {ex}")
            input("Presione Enter para continuar...")