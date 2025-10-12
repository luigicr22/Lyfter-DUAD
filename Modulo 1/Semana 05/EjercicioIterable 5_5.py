list_user = []
highest_number = 0

for index in range(10):
    list_user.append(int(input(f"Ingrese el {index+1}° número: ")))
    if list_user[len(list_user)-1] > highest_number:
            highest_number = list_user[len(list_user)-1]

print(f"{list_user} El más alto fue {highest_number}")