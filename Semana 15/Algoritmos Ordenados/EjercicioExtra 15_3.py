def check_list(func):
    def wrapper(list_sort):
        for item in list_sort:
            if not isinstance (item,int):
                print("Error: La lista solo admite números enteros")
                return
        func(list_sort)
    return wrapper

def check_empty(func):
    def wrapper(list_sort):
        if len(list_sort) == 0:
            print("Error: La lista esta vacia")
            return
        func(list_sort)
    return wrapper

@check_empty
@check_list
def bubble_sort(list_sort):
    print(f"Lista Original:{list_sort}")
    count_iterations = 0
    count_exchanges = 0
    for index_Ext in range(0,len(list_sort)-1):
        is_not_changed = True
        for index in range(0,len(list_sort)-1-index_Ext):
            current_item = list_sort[index]
            next_item = list_sort[index+1]
            if current_item > next_item:
                list_sort[index] = next_item
                list_sort[index+1] = current_item
                is_not_changed = False
                count_exchanges += 1
            count_iterations += 1
        if is_not_changed:
            break
    print(f"Lista Ordenada:{list_sort}")
    print(f"Iteraciones: {count_iterations}")
    print(f"Intercambios: {count_exchanges}")           

print("Lista 1:")
list_one = []
bubble_sort(list_one)

print("\nLista 2:")
list_two = [5,"a", 8]
bubble_sort(list_two)

print("\nLista 3:")
list_three = [5,6,8,7,2,3,4,1,9]
bubble_sort(list_three)