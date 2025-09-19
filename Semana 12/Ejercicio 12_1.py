class BankAccount:
    balance = 0

    def add_balance(self, amount):
        self.balance += amount
        print(f"Agregando fondos.\nBalance actual: {self.balance}\n")

    def subtract_balance(self, amount):
        self.balance -= amount


class SavingAccount(BankAccount):
    def __init__(self,amount):
        self.min_balance = amount
        print(f"Creando cuenta.\nBalance actual: {self.balance}\n")

    def subtract_balance(self, amount):
        if (self.balance - amount) < self.min_balance:
            print(f"No se puede retirar el dinero. Balance restante quedaria menor al minimo permitido de {self.min_balance}")
            print(f"Balance actual: {self.balance}\n")
        else:
            self.balance -= amount
            print(f"Quitando fondos.\nBalance actual: {self.balance}\n")

account = SavingAccount(1000)
account.add_balance (1200)
account.subtract_balance(100)
account.subtract_balance(200)
