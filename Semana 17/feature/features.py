from datetime import date
from feature.objects import Transaction

#Devuelve la lista de todas las transacciones para ser impresa en la interface
def all_transactions(account):
    transactions = []
    headings = ["Fecha","Detalle","Monto","Categoria","Tipo"]
    row_colors = []
    row_counter = 0
    for transaction in account.transactions:
        row = [transaction.date, transaction.details, transaction.amount, transaction.category.category, transaction.type]
        transactions.append(row)
        row_colors.append([row_counter,transaction.category.color])
        row_counter += 1
    all_transactions = [transactions,headings,row_colors]
    return all_transactions


#Devuelve la lista de las transacciones filtradas para ser impresa en la interface
def filter_transactions (account, filter_to_apply):
    if len(filter_to_apply) == 0:
        filtered_transactions = all_categories(account)
    else:
        transactions = []
        headings = ["Fecha","Detalle","Monto","Categoria","Tipo"]
        row_colors = []
        row_counter = 0
        for transaction in account.transactions:
            if ((filter_to_apply['start_date'] <= transaction.date and filter_to_apply['end_date'] >= transaction.date) and (filter_to_apply['category'] == transaction.category.category or filter_to_apply['category'] == "Todas") and (filter_to_apply['type'] == transaction.type or filter_to_apply['type'] == "Todas")):
                row = [transaction.date, transaction.details, transaction.amount, transaction.category.category, transaction.type]
                transactions.append(row)
                row_colors.append([row_counter,transaction.category.color])
                row_counter += 1
        filtered_transactions = [transactions,headings,row_colors]
    return filtered_transactions

#Devuelve una lista de todas las categorias para ser impresa en la interface
def all_categories(account):
    categories = []
    headings = ["Nombre","Color"]
    row_colors = []
    row_counter = 0
    for category in account.categories:
        row = [category.category, category.color]
        categories.append(row)
        row_colors.append([row_counter,category.color])
        row_counter += 1
    all_categories = [categories,headings,row_colors]
    return all_categories


#Lista todas las categorias
def list_categories(account):
    list_categories = []
    categories = account.categories
    for category in categories:
        list_categories.append(category.category)
    return list_categories


#Verifica que todos los campos esten llenos
def check_all_fields_filled (func):
    def wrapper (account, **kwargs):
            if kwargs['transaction_date'] == '' or kwargs['details'] == '' or kwargs['amount'] == '' or kwargs['category'] == '' or kwargs['transaction_type'] == '':
                    raise Exception ('Debe ingresar todos los valores')
            else:
                func(account,**kwargs)
                return account
    return wrapper


#Verifica el monto sea valido
def check_amount (func):
    def wrapper (account, **kwargs):
        try:
            if float(kwargs['amount']) <= 0:
                raise Exception ("El monto debe ser un número mayor a 0")
            else:
                func(account,**kwargs)
                return account
        except ValueError as e:
            raise Exception ("El monto no tiene un formato válido")
    return wrapper


#Agrega una nueva transaccion a la cuenta
@check_all_fields_filled
@check_amount
def add_transaction (account,**kwargs):
    transaction_date = check_date(kwargs['transaction_date'])
    transaction_category = None
    for category in account.categories:
        if category.category == kwargs['category']:
            transaction_category = category
    new_transaction = Transaction (transaction_date, kwargs['details'], float(kwargs['amount']), transaction_category, kwargs['transaction_type'])
    account.add_transaction (new_transaction)
    return account

#Verifica una fecha valida
def check_date (str_date_to_check):
    try:
        list_date_to_check = str_date_to_check.split('-')
        date_to_check = date(int(list_date_to_check[0]),int(list_date_to_check[1]),int(list_date_to_check[2]))
        if date_to_check > date.today():
            raise Exception ("La fecha es mayor a la fecha actual")
        else:
            return date_to_check
    except ValueError as e:
        raise Exception ("La fecha no tiene un formato válido")


#Verifica si las fechas para el filtro son correctas y devuelve diccionario para filtrar.
def check_filter(**kwargs):
    filter_to_apply = {}
    if kwargs['start_date'] == '':
        filter_to_apply['start_date'] = date(1900,1,1)
    else:
        filter_to_apply['start_date'] = check_date(kwargs['start_date'])
    
    if kwargs['end_date'] == '':
        filter_to_apply['end_date'] = date.today()
    else:
        filter_to_apply['end_date'] = check_date(kwargs['end_date'])
    
    if filter_to_apply['start_date'] > filter_to_apply['end_date']:
            raise Exception ("La Fecha inicial no puede ser mayor a la fecha final")

    if kwargs['category'] == '':
        filter_to_apply['category'] = 'Todas'
    else:
        filter_to_apply['category'] = kwargs['category']

    if kwargs['type'] == '':
        filter_to_apply['type'] = 'Todas'
    else:
        filter_to_apply['type'] = kwargs['type']

    return filter_to_apply