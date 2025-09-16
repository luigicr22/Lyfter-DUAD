#Ejercicio 4.1 
#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

first_string = "Hello"
second_string = "World"
first_integer = 5
first_float = 8.5
first_list = [5,7,8]
second_list = [3,9,2]
string_list = ["Hello","World"]
first_bool = True
second_bool = False

#1. string + string → ?
sum_strings = first_string + second_string
print(sum_strings)
#Correct. Add the strings together. 


#2. string + int → ?
#sum_string_int = first_string + first_integer
#TypeError: can only concatenate str (not "int") to str


#3. int + string → ?
#sum_int_string = first_integer + first_string
#TypeError: unsupported operand type(s) for +: 'int' and 'str'


#4. list + list → ?
sum_lists = first_list + second_list
print(sum_lists)
#Correct. Add the lists together. 


#5. string + list → ?
#sum_string_list = first_string + first_list
#TypeError: can only concatenate str (not "list") to str

#sum_string_list = first_string + string_list
#With a list of strings, it shows the same error.= TypeError: can only concatenate str (not "list") to str


#6. float + int → ?
sum_float_int = first_float + first_integer
print(sum_float_int)
#Correct. Add float and integer as a float.

#7. bool + bool → ?
sum_bool_bool = first_bool + second_bool
print(sum_bool_bool)
sum_bool_bool = first_bool + first_bool
print(sum_bool_bool)
sum_bool_bool = second_bool + second_bool
print(sum_bool_bool)
sum_integer_bool = first_integer + first_bool
print(sum_integer_bool)
#It takes Boolean values as numbers (False = 0, True = 1) and adds them together.
#A Boolean value can be added to an integer.
