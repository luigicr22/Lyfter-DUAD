list_user = []

while (True):
    list_user.append(int(input(f"Ingrese un número a la lista: ")))
    one_more = input("Presione Enter si desea continuar ingresando números a la lista, o digite 'N' para concluir: ")
    if one_more == "N":
        break

lowest_number = list_user[0]

for record in list_user:
    if record < lowest_number:
        lowest_number = record

print(list_user)
print(f"El menor valor es {lowest_number}")