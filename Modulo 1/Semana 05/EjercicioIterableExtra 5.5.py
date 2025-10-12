list_user = []

for index in range(5):
    list_user.append(input(f"Ingrese la {index+1}° palabra: "))

new_list = []
for record in list_user:
    if len(record) > 4:
        new_list.append(record)

print(f"La lista original fue {new_list}")
print(f"La lista con palabras de más de 4 letras es: {new_list}")