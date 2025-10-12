list_user = []

while (True):
    list_user.append(int(input(f"Ingrese un número a la lista: ")))
    one_more = input("Presione Enter si desea continuar ingresando números a la lista, o digite 'N' para concluir: ")
    if one_more == "N":
        break

all_positives = True
for record in list_user:
    if record <= 0:
        all_positives = False
        break

if all_positives:
    print("Todos los números son positivos")
else:
    print("Hay al menos un número negativo o cero")