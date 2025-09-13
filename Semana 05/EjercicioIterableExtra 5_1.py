list_user = []

while (True):
    list_user.append(int(input(f"Ingrese un número a la lista: ")))
    one_more = input("Presione Enter si desea continuar ingresando números a la lista, o digite 'N' para concluir: ")
    if one_more == "N":
        break

find_number = int(input("Que número desea buscar: "))
count_number = 0
for record in list_user:
    if record == find_number:
        count_number += 1

print(f"La lista fue la siguiente: {list_user}")
print(f"El número {find_number} aparece {count_number} veces")
