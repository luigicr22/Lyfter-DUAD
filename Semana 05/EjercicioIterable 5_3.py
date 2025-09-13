my_list = [4, 3, 6, 1, 7]

temporary = my_list[0]
my_list [0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = temporary

print(my_list)
