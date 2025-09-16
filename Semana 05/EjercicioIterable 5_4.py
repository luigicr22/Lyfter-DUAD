my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11]

index = 0
while (index < len(my_list)):
    if (my_list[index]%2 != 0):
        my_list.pop(index)
    else:
        index += 1

print(my_list)