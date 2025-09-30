import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modulos import Ejercicio16_2


#Semana 6 Ejercicio #3 
def test_sum_list_all_positives ():
 # Arrange
    list_to_sum = [4, 6, 2, 29]
    # Act
    result = Ejercicio16_2.sum_list (list_to_sum)
    # Assert
    assert result == 41

def test_sum_list_all_negatives ():
 # Arrange
    list_to_sum = [-4, -6, -2, -29]
    # Act
    result = Ejercicio16_2.sum_list (list_to_sum)
    # Assert
    assert result == -41

def test_sum_list_positive_negative_zero ():
 # Arrange
    list_to_sum = [-4, -6, 0, 29]
    # Act
    result = Ejercicio16_2.sum_list (list_to_sum)
    # Assert
    assert result == 19


#Semana 6 Ejercicio #4
def test_reverse_string_with_all_lower ():
    # Arrange
    word = "hola mundo"
    # Act
    result = Ejercicio16_2.reverse_string(word)
    # Assert
    assert result == "odnum aloh"

def test_reverse_string_with_all_upper ():
    # Arrange
    word = "HOLA MUNDO"
    # Act
    result = Ejercicio16_2.reverse_string(word)
    # Assert
    assert result == "ODNUM ALOH"

def test_reverse_string_with_char_and_numbers ():
    # Arrange
    word = "Hola muN2"
    # Act
    result = Ejercicio16_2.reverse_string(word)
    # Assert
    assert result == "2Num aloH"


#Semana 6 Ejercicio #5
def test_count_cases_with_all_upper ():
    # Arrange
    original_string = "I LOVE NACION SUCHI"
    # Act
    result = Ejercicio16_2.count_cases(original_string)
    # Assert
    assert result == ({"count_upper":16,"count_lower":0})

def test_count_cases_with_all_lower ():
    # Arrange
    original_string = "i love nación sushi"
    # Act
    result = Ejercicio16_2.count_cases(original_string)
    # Assert
    assert result == ({"count_upper":0,"count_lower":16})

def test_count_cases_with_char_and_numbers ():
    # Arrange
    original_string = "I love Nación Sushi,2"
    # Act
    result = Ejercicio16_2.count_cases(original_string)
    # Assert
    assert result == ({"count_upper":3,"count_lower":13})


#Semana 6 Ejercicio #6
def test_sort_string_all_lower():
    # Arrange
    string_original = "python-variable-funcion-computadora-monitor"
    # Act
    result = Ejercicio16_2.sort_string(string_original)
    # Assert
    assert result == 'computadora-funcion-monitor-python-variable'

def test_sort_string_all_upper():
    # Arrange
    string_original = "PYTHON-VARIABLE-FUNCION-COMPUTADORA-MONITOR"
    # Act
    result = Ejercicio16_2.sort_string(string_original)
    # Assert
    assert result == 'COMPUTADORA-FUNCION-MONITOR-PYTHON-VARIABLE'

def test_sort_string_char_and_numbers():
    # Arrange
    string_original = "PYTHON-variable-FUNCION2-COMPUtadora/MONITOR"
    # Act
    result = Ejercicio16_2.sort_string(string_original)
    # Assert
    assert result == 'COMPUtadora/MONITOR-FUNCION2-PYTHON-variable'

#Semana 6 Ejercicio #7
def test_is_prime_all_prime():
    # Arrange
    original_list = [2, 3, 5, 7, 11, 13, 17]
    # Act
    result = Ejercicio16_2.check_list(original_list)
    # Assert
    assert result == [2, 3, 5, 7, 11, 13, 17]

def test_is_prime_not_primes():
    # Arrange
    original_list = [0, 1, 4, 6, 8, 9, 10, 12]
    # Act
    result = Ejercicio16_2.check_list(original_list)
    # Assert
    assert result == []

def test_is_prime_mix_numbers():
    # Arrange
    original_list = [1, 4, 6, 7, 13, 9, 67]
    # Act
    result = Ejercicio16_2.check_list(original_list)
    # Assert
    assert result == [7, 13, 67]


#Semana 6 Ejercicio Extra #1
def test_count_char_all_lower():
    # Arrange
    original_string = "hola mundo"
    char_to_find = 'o'
    # Act
    result = Ejercicio16_2.count_char(original_string,char_to_find)
    # Assert
    assert result == 2

def test_count_char_all_upper():
    # Arrange
    original_string = "HOLA MUNDO"
    char_to_find = 'o'
    # Act
    result = Ejercicio16_2.count_char(original_string,char_to_find)
    # Assert
    assert result == 0

def test_count_upper_and_lower():
    # Arrange
    original_string = "hola MUNDO"
    char_to_find = 'o'
    # Act
    result = Ejercicio16_2.count_char(original_string,char_to_find)
    # Assert
    assert result == 1


#Semana 6 Ejercicio Extra #2
def test_is_len_than_all_longer ():
    # Arrange
    original_list = ['Lista','de','palabras','mas','larga']
    len_than = 1
    # Act
    result = Ejercicio16_2.is_len_than(original_list,len_than)
    # Assert
    assert result == ['Lista','de','palabras','mas','larga']

def test_is_len_than_all_shorter ():
    # Arrange
    original_list = ['Lista','de','palabras','mas','larga']
    len_than = 8
    # Act
    result = Ejercicio16_2.is_len_than(original_list,len_than)
    # Assert
    assert result == []

def test_is_len_than_with_empty_string ():
    # Arrange
    original_list = ['Lista','de','','mas','larga']
    len_than = 3
    # Act
    result = Ejercicio16_2.is_len_than(original_list,len_than)
    # Assert
    assert result == ['Lista','larga']


#Semana 6 Ejercicio Extra #3
def test_count_vowels_all_vowels ():
    # Arrange
    original_string = "AoUiAEeoi"
    # Act
    result = Ejercicio16_2.count_vowels (original_string)
    # Assert
    assert result == 9

def test_count_vowels_without_vowels ():
    # Arrange
    original_string = "Hwlh pmlndq"
    # Act
    result = Ejercicio16_2.count_vowels (original_string)
    # Assert
    assert result == 0

def test_count_vowels_only_lower ():
    # Arrange
    original_string = "hola mundo"
    # Act
    result = Ejercicio16_2.count_vowels (original_string)
    # Assert
    assert result == 4