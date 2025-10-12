def bubble_sort(list_sort):
    for index_Ext in range(len(list_sort)-1,0,-1):
        is_not_changed = True
        for index in range(len(list_sort)-1,len(list_sort)-index_Ext-1,-1):
            current_item = list_sort[index]
            previous_item = list_sort[index-1]
            if current_item < previous_item:
                list_sort[index] = previous_item
                list_sort[index-1] = current_item
                is_not_changed = False
            print(f"{index_Ext}-{index}={list_sort}")
        if is_not_changed:
            break           

test_list = [9,8,7,6,5,4,3,2,1]
print(test_list)
bubble_sort(test_list)
print(test_list)