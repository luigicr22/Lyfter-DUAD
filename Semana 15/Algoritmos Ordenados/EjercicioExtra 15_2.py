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

test_list = [5,6,8,7,2,3,4,1,9]
bubble_sort(test_list)