import pytest
from unittest.mock import mock_open, patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modulos import EjercicioExtra16_4


def test_read_lines_success():
    # Arrange
    mock_data = "línea 1\nlínea 2\nlínea 3\n"
    # Act
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = EjercicioExtra16_4.read_lines("archivo.txt")
    #Assert
    assert result == ["línea 1\n", "línea 2\n", "línea 3\n"]

def test_read_lines_file_not_found():
    # Arrange & Act & Arrange
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            EjercicioExtra16_4.read_lines("archivo.txt")
