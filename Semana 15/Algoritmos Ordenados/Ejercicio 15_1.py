def bubble_sort(list_sort):
    for index_Ext in range(0,len(list_sort)-1):
        is_not_changed = True
        for index in range(0,len(list_sort)-1-index_Ext):
            current_item = list_sort[index]
            next_item = list_sort[index+1]
            if current_item > next_item:
                list_sort[index] = next_item
                list_sort[index+1] = current_item
                is_not_changed = False
            print(f"{index_Ext}-{index}={list_sort}")
        if is_not_changed:
            break
    return  list_sort           

test_list = [9,8,7,6,5,4,3,2,1]
print(test_list)
test_list = bubble_sort(test_list)
print(test_list)