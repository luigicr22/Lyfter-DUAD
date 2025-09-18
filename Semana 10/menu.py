import os
from feature import actions

def start_menu ():
    while True:
        os.system('cls')
        print("""
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
                    actions.add_students()
                case 2:
                    return 'remove_student'
                case 3:
                    return 'view_students'
                case 4:
                    return 'view_top_students'
                case 5:
                    return 'view_average_grades'
                case 6:
                    return 'view_failed_students'
                case 7:
                    return 'import_data'
                case 8:
                    return 'export_data'
                case 9:
                    save_before = input("Desea exportar los datos antes de salir? (Presione \"s\" para exportar): ")
                    if save_before.lower() == 's':
                        return 'export_data'
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