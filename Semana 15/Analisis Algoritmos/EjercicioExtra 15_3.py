def print_all_pairs(my_dict): #O(n^2)
    for key1 in my_dict: #O(n)
        for key2 in my_dict: #O(n^2)
            print(f"{key1}-{key2}") #O(1)

#Complejidad de la versión: Algoritmo O(log n)
#Para 1 000 000 de llaves, tiene que hacer 1 000 000 000 000 de iteraciones, ya que es exponencial 