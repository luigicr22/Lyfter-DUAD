def is_valid_name(name):
    if name == "":
        print("El nombre completo no puede estar vacío.")
        return False

    name = name.split()
    if len(name) < 2:
        print("Debe ingresar al menos un nombre y un apellido.")
        return False
    
    for part in name:
        if not part.isalpha():
            print("El nombre completo solo puede contener letras.")
            return False
        
    print("Nombre válido.")
    return True


def is_valid_section(section):
    if section  == "":
        print("La sección no puede estar vacía.")
        return False
    try:
        section = section.split('-')
        section[0] = int(section[0])

        if section[0] < 1 or section[0] > 13:
            print("El número de la sección debe estar entre 1 y 12.")
            return False
        
        if (not section[1].isalpha()) or len(section[1]) != 1:
            print("La sección debe tener una sola letra.")
            return False
        
        if len(section) > 2:
            print("El formato de la sección es inválido. Debe ser como 10-A, 11-B, etc.")
            return False
    
    except IndexError:
        print("El formato de la sección es inválido. Debe ser como 10-A, 11-B, etc.")
        return False
    
    except ValueError:
        print("El formato de la sección es inválido. Debe ser como 10-A, 11-B, etc.")
        return False
    
    print("Sección válida.")
    return True


def exist_student(student, students):
    for pupil in students:
        if pupil.get('full_name') == student.get('full_name'):
            if pupil.get('section') == student.get('section'):
                print("El estudiante existe en esa sección.")
                return True
            else:
                add_student = input(f"El estudiante existe en la sección {pupil.get('section')}. Presione \"S\" si desea contnuar de todos modos: ")
                if add_student == "S":
                    return False
                else:
                    return True
    return False


def input_grade (subject):
    while True:
        try:
            grade = {}
            grade['subject'] = subject
            grade['grade'] = int (input(f"Ingrese la nota de {subject}: "))
            if grade.get('grade') >= 0 and grade.get('grade') <= 100:
                return grade
            else:
                print("La nota debe ser un número entre 0 y 100.")
        
        except ValueError:
            print("La nota debe ser un número entre 0 y 100.")


def calculate_average(grades):
    average = 0

    for grade in grades:
        average += grade.get('grade')

    average /= len(grades)
    return average


def exist_remove(student, students):
    for pupil in students:
        if pupil.get('full_name') == student.get('full_name'):
            if pupil.get('section') == student.get('section'):
                print("El estudiante existe en esa sección.")
                remove = input("Presione \"E\" para confirmar que desea eliminar el estudiante: ")
                if remove == "E":
                    students.remove(pupil)
                    input("ESTUDIANTE ELIMINADO. Presione cualquier tecla para continuar...")
                    return students
                else:
                    input("No se eliminará el estudiante seleccionado. Presione Enter para continuar...")
                return students
    input("El estudiante no existe. Presione Enter para continuar...")
    return students