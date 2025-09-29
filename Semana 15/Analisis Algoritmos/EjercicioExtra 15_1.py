#Version 1
def manual_add(number): #O(n)
    result = 0 #O(1)
    for i in range(1, number + 1): #O(n)
        result += i #O(1)
    return result #O(1)

#Complejidad de la versión: Algoritmo O(n)



#Version 2
def add_formula(number):
    return number * (number + 1) // 2 #O(1)

#Complejidad de la versión: Algoritmo O(1)
#Usaria esta version para multiplicar number = 1 000 000 000, ya que no depende del tamaño del número el tiempo, siempre es la misma complejidad la función