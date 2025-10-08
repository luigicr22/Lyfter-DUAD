from datetime import date


class Transaction():
    def __init__(self, transaction_date, details, amount, category,transaction_type):
        self._transaction_date = transaction_date
        self._details = details
        self._amount = amount
        self._category = category
        self._transaction_type = transaction_type
    
    @property
    def date (self):
        return self._transaction_date
    
    @property
    def details (self):
        return self._details

    @property
    def amount (self):
        return self._amount
    
    @property
    def category(self):
        return self._category

    @property
    def type (self):
        return self._transaction_type



class Category():
    def __init__(self, category_name, color):
        self._category_name = category_name
        self._color = color

    @property
    def category (self):
        return self._category_name
    
    @property
    def color (self):
        return self._color
    
    def update_category (self, category_name, color):
        self._category_name = category_name
        self._color = color


class Account():
    def __init__(self, account_name):
        self._account_name = account_name
        self._account_transactions = []
        self._account_categories = []
    
    @property
    def name (self):
        return self._account_name
    
    @property
    def transactions(self):
        return self._account_transactions
    
    @property
    def categories(self):
        return self._account_categories
    
    def add_transaction (self,transaction):
        self._account_transactions.append(transaction)

    
    def add_category (self,category):
        self._account_categories.append(category)