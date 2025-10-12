import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modulos import EjercicioExtra16_3

def test_divide_all_positives():
# Arrange
    number1=10
    number2=2
    # Act
    result = EjercicioExtra16_3.divide(number1,number2)
    # Assert
    assert result == 5

def test_divide_zero():
# Arrange
    number1=10
    number2=0
    # Act & Assert
    with pytest.raises(ValueError):
        EjercicioExtra16_3.divide(number1,number2)

def test_divide_zero():
# Arrange
    number1=10
    number2='zero'
    # Act & Assert
    with pytest.raises(TypeError):
        EjercicioExtra16_3.divide(number1,number2)

