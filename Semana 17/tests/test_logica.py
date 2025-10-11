import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from feature import features, objects, persistence
from datetime import date

#general Arrange
category1 = objects.Category("Salarios","#22f8ff")
category2 = objects.Category("Hormiga",'#933CC2')
transaction1 = objects.Transaction(date(2025,9,11),"Salario",100000.0,category1,"Ingreso")
transaction2 = objects.Transaction(date(2024,9,11),"Super",1000.0,category2,"Gasto")
account = objects.Account("Luis")
account._account_transactions.append(transaction1)
account._account_categories.append(category1)
account._account_transactions.append(transaction2)
account._account_categories.append(category2)

def test_all_categories_correct():
    # Arrange
    account_test = account
    all_categories = [
        [["Salarios","#22f8ff"],["Hormiga",'#933CC2']],
        ["Nombre","Color"],
        [[0,"#22f8ff"],[1,'#933CC2']]
    ]

    # Act
    transactions = features.all_categories(account_test)

    # Assert
    assert all_categories == transactions


def test_check_all_fields_filled_missing():
    # Arrange
    kwargs = {
        'transaction_date': '2023-01-01',
        'details': '',
        'amount': '100',
        'category': 'Alimentos',
        'transaction_type': 'Ingreso'
    }

    # Act
    with pytest.raises(Exception) as e:
        features.add_transaction(account, **kwargs)
    
    # Assert
    assert 'Debe ingresar todos los valores' in str(e.value)


def test_check_amount_negative():
    # Arrange
    kwargs = {
        'transaction_date': '2023-01-01',
        'details': 'Compras',
        'amount': '-100',
        'category': 'Alimentos',
        'transaction_type': 'Ingreso'
    }

    # Act
    with pytest.raises(Exception) as e:
        features.add_transaction(account, **kwargs)
    
    # Assert
    assert 'El monto debe ser un número mayor a 0' in str(e.value)


def test_check_amount_invalid_format():
    # Arrange
    kwargs = {
        'transaction_date': '2023-01-01',
        'details': 'Compras',
        'amount': 'cien',
        'category': 'Alimentos',
        'transaction_type': 'Ingreso'
    }
    
    # Act
    with pytest.raises(Exception) as e:
        features.add_transaction(account, **kwargs)
    
    # Assert
    assert 'El monto no tiene un formato válido' in str(e.value)


def test_check_date_future_date():
    # Arrange
    date_to_test = '2030-10-8'
    
    # Act
    with pytest.raises(Exception) as e:
        features.check_date(date_to_test)
    
    # Assert
    assert 'La fecha es mayor a la fecha actual' in str(e.value)


def test_check_date_invalid_format():
    # Arrange
    date_to_test = 'miercoles 8 de octubre'
    
    # Act
    with pytest.raises(Exception) as e:
        features.check_date(date_to_test)
    
    # Assert
    assert 'La fecha no tiene un formato válido' in str(e.value)


def test_check_filter_start_date_greater_than_end_date():
    # Arrange
    kwargs = {
        'start_date': '2025-10-8',
        'end_date': '2025-10-1',
        'category': '',
        'type' : ''
    }
    
    # Act
    with pytest.raises(Exception) as e:
        features.check_filter(**kwargs)
    
    # Assert
    assert 'La Fecha inicial no puede ser mayor a la fecha final' in str(e.value)


def test_check_filter_future_start_date():
    # Arrange
    kwargs = {
        'start_date': '2026-10-8',
        'end_date': '',
        'category': '',
        'type' : ''
    }
    
    # Act
    with pytest.raises(Exception) as e:
        features.check_filter(**kwargs)
    
    # Assert
    assert 'La fecha es mayor a la fecha actual' in str(e.value)