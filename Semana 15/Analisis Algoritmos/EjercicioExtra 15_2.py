#Algoritmo 1
def linear_search(my_list, target): #O(n)
    for item in my_list: #O(n)
        if item == target: #O(1)
            return True #O(1)
    return False #O(1)

#Complejidad de la versión: Algoritmo O(n)
#Este conviene usarlo cuando la lista no esta ordena, ya que la recorre toda.
#Si la lista no esta ordenada, incluso puede reducir el tiempo si lo encuentra en la primera iteracion.


#Algoritmo 2
def binary_search(my_list, target):
    low = 0 #O(1)
    high = len(list) - 1 #O(1)
    while low <= high: #O(log n)
        mid = (low + high) // 2
        if my_list[mid] == target: #O(1)
            return True #O(1)
        elif my_list[mid] < target: #O(1)
            low = mid + 1 #O(1)
        else: #O(1)
            high = mid - 1 #O(1)
    return False #O(1)

#Complejidad de la versión: Algoritmo O(log n)
#Si la lista esta ordenada, es bastante eficiente porque en cada iteracion reduce la lista a la mitad.
#Si la lista no esta ordena, puede existir escenarios donde no encuentre el valor buscado aunque exista.

