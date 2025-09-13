first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

tercera = first_list + second_list
print(tercera)
for index in range(0, len(first_list)):
    print(f"{first_list[index]} {second_list[index]}")