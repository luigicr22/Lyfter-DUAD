#Semana 6 Ejercicio #3 
def sum_list (list_to_sum):
    total_sum = 0
    for number in list_to_sum:
        total_sum += number
    return total_sum


#Semana 6 Ejercicio #4
def reverse_string (string_to_reverse):
    string_reversed = ""
    for char in range (len(string_to_reverse)-1,-1,-1):
        string_reversed += string_to_reverse[char]
    return string_reversed


#Semana 6 Ejercicio #5
def count_cases (string_to_count):
    count_upper = 0
    count_lower = 0
    for char in string_to_count:
        if str(char).isupper():
            count_upper += 1
        elif str(char).islower():
            count_lower += 1
    return({"count_upper":count_upper,"count_lower":count_lower})


#Semana 6 Ejercicio #6
def sort_string(string_original):
    print(f"String original= {string_original}")
    list_original = convert_to_list (string_original)
    print(f"Lista original= {list_original}")
    list_sorted = sort_list(list_original)
    print(f"Lista ordenada= {list_sorted}")
    string_sorted = convert_to_string(list_sorted)
    return string_sorted

def convert_to_list(string_original):
    list_original = string_original.split("-")
    return (list_original)

def sort_list(list_original):
    list_original.sort()
    return (list_original)

def convert_to_string(list_sorted):
    string_sorted = ""
    for index in range(len(list_sorted)):
        string_sorted += list_sorted[index]
        if index < (len(list_sorted)-1):
            string_sorted += "-"
    return string_sorted


#Semana 6 Ejercicio #7
def is_prime (number):
    if number == 1 or number == 0:
        is_prime = False
    elif number == 2 or number == 3 or number == 5:
        is_prime = True
    elif number%2 == 0 or number%3 == 0 or number%5 == 0:
        is_prime = False
    elif ((number**(1/2))%1) == 0:
        is_prime = False
    else:
        is_prime = True
        for index in range(3,int((number**(1/2))+1)):
            if number%(index) == 0:
                is_prime = False
                break
    return (is_prime)

def check_list (list_to_check):
    list_prime = []
    for number in list_to_check:
        if is_prime(number):
            list_prime.append(number)
    return (list_prime)


#Semana 6 Ejercicio Extra #1
def count_char (original_string, char_to_find):
    count = str(original_string).count(char_to_find)
    return count


#Semana 6 Ejercicio Extra #2
def is_len_than (original_list,len_than):
    list_len_than = []
    for string in original_list:
        if len(string) > len_than:
            list_len_than.append(string)
    return (list_len_than)


#Semana 6 Ejercicio Extra #3
def count_vowels (string_original):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    for char in string_original:
        if char in vowels:
            count_vowels += 1
    return count_vowels