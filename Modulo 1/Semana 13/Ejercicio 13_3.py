import datetime

class User:

    def __init__(self, year, month, day):
        self._date_of_birt = datetime.datetime(year, month, day)
    
    @property
    def age(self):
        age = ((datetime.datetime.now() - self._date_of_birt).days/365)
        return age
    
    def check_age(func):
        def wrapper (self, user):
            if user.age >= 18:
                func(self,user)
            else:
                print("El usuario es menor de edad")
        return wrapper

    @check_age
    def check_user(self, user):
        print ("El usuario es mayor de edad")

user1 = User(2015,4,22)
print(f"{user1.age:.0f} años")
user1.check_user(user1)
print("\n")
user2 = User(1987,4,22)
print(f"{user2.age:.0f} años")
user2.check_user(user2)