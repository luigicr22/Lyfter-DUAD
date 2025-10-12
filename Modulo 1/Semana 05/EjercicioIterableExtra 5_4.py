list_user = []
average = 0

while (True):
    list_user.append(int(input(f"Ingrese un número a la lista: ")))
    one_more = input("Presione Enter si desea continuar ingresando números a la lista, o digite 'N' para concluir: ")
    average += list_user[len(list_user)-1]
    if one_more == "N":
        break

average = average / len(list_user)

new_list = []
for record in list_user:
    if record > average:
        new_list.append(record)

print(list_user)
print(f"El promedio es {average:.2f}")
print(f"La nueva lista es: {new_list}")