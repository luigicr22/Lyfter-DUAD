import os
from datetime import date
from feature.objects import Transaction, Account, Category
import FreeSimpleGUI as sg

import csv

def check_file (func):
    def wrapper ():
        if os.path.exists('GestorFinanzasTransacciones.cvs') and os.path.exists('GestorFinanzasCategorias.cvs'):
            return func()
        else:
            account = new_account()
            return account
    return wrapper

def new_account ():
    while True:
        name = sg.popup_get_text('No se encuentran los archivos existente necesarios.\nIngrese un nombre para la una nueva cuenta:')
        if name:
            break
    account = Account(name)
    return account

@check_file
def load_account ():
    account = None
    try:
        with open('GestorFinanzasCategorias.cvs','r', encoding='utf-8') as file:
            reader = csv.DictReader (file)
            for row in reader:
                if account == None:
                    account = Account(row['account_name'])
                category_name = row['category_name']
                color = row['color']
                category = Category(category_name,color)
                account.add_category(category)
        
        with open('GestorFinanzasTransacciones.cvs','r', encoding='utf-8') as file:
            reader = csv.DictReader (file)
            for row in reader:
                row_date = row['transaction_date'].split('-')
                transaction_date = date(int(row_date[0]),int(row_date[1]),int(row_date[2]))
                details = row['details']
                amount = float(row['amount'])
                exist_category = False
                for category_existed in account.categories:
                    if category_existed.category == row['category']:
                        category = category_existed
                        exist_category = True
                        break
                if exist_category:
                    transaction_type = row['transaction_type']
                    transaction = Transaction(transaction_date, details, amount, category,transaction_type)
                    account.add_transaction(transaction)
                else:
                    raise FileNotFoundError
        return account
    except FileNotFoundError:
        print("Error en la integridad de los datos")
        exit()


def save_account(account):
    headers = ['account_name', 'transaction_date', 'details', 'amount', 'category', 'transaction_type']
    with open('GestorFinanzasTransacciones.cvs','w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        for transaction in account.transactions:
            transaction_row = {}
            transaction_row['account_name']=account.name
            transaction_row['transaction_date']=transaction.date
            transaction_row['details']=transaction.details
            transaction_row['amount']=transaction.amount
            transaction_row['category']=transaction.category.category
            transaction_row['transaction_type']=transaction.type            
            writer.writerow(transaction_row)
    
    headers = ['account_name','category_name', 'color']
    with open('GestorFinanzasCategorias.cvs','w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        for category in account.categories:
            category_row = {}
            category_row['account_name']=account.name
            category_row['category_name']=category.category
            category_row['color']=category.color      
            writer.writerow(category_row)
    return True


def account_statement (account):
    headers = ['Fecha', 'Detalle', 'Monto', 'Categoría', 'Tipo']
    with open('EstadoCuenta.cvs','w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        total_expense = 0
        total_income = 0
        balance = 0
        writer.writeheader()
        for transaction in account.transactions:
            transaction_row = {}
            transaction_row['Fecha']=transaction.date
            transaction_row['Detalle']=transaction.details
            transaction_row['Monto']=transaction.amount
            transaction_row['Categoría']=transaction.category.category
            transaction_row['Tipo']=transaction.type            
            writer.writerow(transaction_row)
            if transaction.type == "Ingreso":
                total_income += transaction.amount
            else:
                total_expense += transaction.amount
        balance = total_income - total_expense
        write_totals = csv.writer(file)
        write_totals.writerow(["Totales:"])
        write_totals.writerow([f"Total Ingresos: {total_income}"])
        write_totals.writerow([f"Total Gastos: {total_expense}"])
        write_totals.writerow([f"Balance: {balance}"])

    return True
