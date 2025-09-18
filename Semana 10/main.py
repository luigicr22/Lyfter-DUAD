#{
# "name" : "Nombre",
# "lastname" : "apellido",
# "class" : "Clase",
# "grades" : 
#       [
#       {"subject" : "spanish", "grade" : 0},
#       {"subject" : "english", "grade" : 0},
#       {"subject" : "history", "grade" : 0},
#       {"subject" : "science", "grade" : 0}
#       ],
# "average_grade" : 0
#}

# Este debe tener un menu que me permita accesar a todas las funciones (**deberá validar que se ingrese una opción del valida del menú**):

# 1. Ingresar información de `n` cantidad de estudiantes, *uno por uno*.
# - Incluir un ciclo para ingresar `n` cantidad de estudiantes.
#      1. Cada estudiante debe incluir:
#         1. Nombre completo
#- Que el nombre completo no esté vacío ni tenga números
#         2. Sección (ejemplo: *11-B*)
#  - Que la sección siga el formato válido (ejemplo: "10-A", "11-B", etc.)
# - Que la sección no esté vacía y siga el formato correcto
#- Que los numeros sean de 1 a 12
#         3. Nota de español
#         4. Nota de inglés
#         5. Nota de sociales
#         6. Nota de ciencias
#- Deberá validar que las notas ingresadas sean validas (números de 0 a 100) y seguir pidiéndola hasta que sea valida.
#- Al finalizar las notas, calcular el promedio de las notas y guardarlo en el campo `average_grade`.
#       
# - Que no se permita ingresar dos estudiantes con el **mismo nombre y sección** (no duplicados)
# - Que si existe el estudiante, se indique que ya esta en una seccion antes agregarlo en otra seccion.
#     - *Tip:* Puede hacer una función `is_valid_name`, `is_valid_section` y `student_exists`








# 2. Ver la información de todos los estudiantes ingresados.
#- Recorrer todos los estudiantes y mostrar su información en un formato amigable.


# 3. Ver el top 3 de los estudiantes con la mejor nota promedio (*es decir, el promedio de su* `nota de español`+ `nota de inglés` + `nota de sociales` + `nota de ciencias`).
#- recorrer todos los estudiantes y comparar con el tercero.
#- si es mayor o igual al tercero, compararlo con el top 3.
#- Si es igual a alguno acomodarlos por orden alfabético.
#- Actualizar los restantes del top 3 si es necesario.


# 4. Ver la nota promedio entre las notas de todos los estudiantes (es decir, el promedio del `promedio de notas` *de cada uno*).
#- recorrer todos los estudiantes y sacar el promedio de sus promedios




# 5. Exportar todos los datos actuales a un archivo CSV.




# 6. Importar los datos de un archivo CSV previamente exportado.
#     1. Si no hay un archivo previamente exportado, debe de decírselo al usuario.
#  -Check que exista un archivo antes de importarlo (Try - Except)


# 7. **Agregue una opción nueva al menú que permita eliminar a un estudiante usando su nombre y sección**
# - Debe validar:
#     - Si el estudiante existe o no
#   - si existe el estudiante pero no es la seccion seleccionada, avisar que existe uno pero no es igual.
#     - Confirmar con el usuario antes de eliminar




# 8. **Mostrar estudiantes reprobados**
#- Listar todos los estudiantes que tengan al menos una materia con nota menor a 60
# - Añada una opción al menú: `Ver estudiantes reprobados`
# - Recorra todos los estudiantes y revise si alguna de las 4 materias tiene notas menores a 60
# - Muestre el nombre, sección y las materias reprobadas con sus notas



# Divida el proyecto en los siguientes módulos:

# - `main`: tendrá el punto de entrada del programa.
# - `menu`: tendrá toda la lógica relacionada al menu de opciones.
# - `actions`: tendrá toda la lógica de las acciones del menu, excepto las de exportar e importar datos.
# - `data`: tendrá toda la lógica de exportación e importación de datos. 

from menu import start_menu


def main ():
    start_menu()


if __name__ == "__main__":
    main()