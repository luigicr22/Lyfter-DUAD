import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modulos.Ejercicio16_1 import bubble_sort


def test_bubble_sort_all_positive_numbers():
    # Arrange
    test_list = [9,8,7,6,5,4,3,2,1]

    # Act
    sort_list = bubble_sort(test_list)

    # Assert
    assert sort_list == [1,2,3,4,5,6,7,8,9]


def test_bubble_sort_all_negative_numbers():
    # Arrange
    test_list = [-1,-2,-3,-4,-5,-6,-7,-8,-9]

    # Act
    sort_list = bubble_sort(test_list)

    # Assert
    assert sort_list == [-9,-8,-7,-6,-5,-4,-3,-2,-1]


def test_bubble_sort_all_zero():
    # Arrange
    test_list = [0,0,0,0,0,0,0,0,0]

    # Act
    sort_list = bubble_sort(test_list)

    # Assert
    assert sort_list == [0,0,0,0,0,0,0,0,0]


def test_bubble_sort_positive_negative_zero_numbers():
    # Arrange
    test_list = [-5,8,0,9,-1,3,7,8,0]

    # Act
    sort_list = bubble_sort(test_list)

    # Assert
    assert sort_list == [-5,-1,0,0,3,7,8,8,9]