class Greet:

    def repeat_twice (func):
        def wrapper (self,name):
            func(self,name)
            func(self,name)
        return wrapper

    @classmethod
    @repeat_twice
    def greeting (cls,name):
        print(f"Hola {name}")

Greet.greeting ("Luis")