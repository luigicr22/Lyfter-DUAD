import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modulos import EjercicioExtra16_1

def test_function_sum_all_positive():
    # Arrange
    number1=10
    number2=2
    # Act
    result = EjercicioExtra16_1.function_sum (number1,number2)
    # Assert
    assert result == 12

def test_function_sum_all_negative():
    # Arrange
    number1=-10
    number2=-2
    # Act
    result = EjercicioExtra16_1.function_sum (number1,number2)
    # Assert
    assert result == -12

def test_function_sum_with_zero():
    # Arrange
    number1=10
    number2=0
    # Act
    result = EjercicioExtra16_1.function_sum (number1,number2)
    # Assert
    assert result == 10


def test_function_average_all_positive ():
    # Arrange
    numbers = [5,15,11,9]
    # Act
    result = EjercicioExtra16_1.function_average (numbers)
    # Assert
    assert result == 10

def test_function_average_all_negative ():
    # Arrange
    numbers = [-5,-15,-11,-9]
    # Act
    result = EjercicioExtra16_1.function_average (numbers)
    # Assert
    assert result == -10

def test_function_average_with_Zeros():
    # Arrange
    numbers = [5,15,0,9]
    # Act
    result = EjercicioExtra16_1.function_average (numbers)
    # Assert
    assert result == 9


def test_function_modulus_all_positive():
    # Arrange
    number1=10
    number2=2
    # Act
    result = EjercicioExtra16_1.function_modulus(number1,number2)
    # Assert
    assert result == 0

def test_function_modulus_all_negatives():
    # Arrange
    number1=-10
    number2=-2
    # Act
    result = EjercicioExtra16_1.function_modulus(number1,number2)
    # Assert
    assert result == 0

def test_function_modulus_wit_Zero():
    # Arrange
    number1=10
    number2=0
    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        EjercicioExtra16_1.function_modulus(number1,number2)