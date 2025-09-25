class Greet:

    def repeat_twice (func):
        def wrapper (self,name,*args):
            print(func(self,name))
            print(func(self,name))
        return wrapper

    @classmethod
    @repeat_twice
    def greeting (cls,name):
        return f"Hola {name}"

Greet.greeting ("Luis")
Greet.greeting ("Ana","Maria")