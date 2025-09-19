class Animal:
    def __init__(self):
        self.breathe = True
    def can(self,name):
        print(f"\nEl {name} puede:\n-Respirar")


class Flyer:
    def __init__(self):
        self.fly = True
    def can_fly(self):
        print("-Volar")


class Swimmer:
    def __init__(self):
        self.swim = True
    def can_swim(self):
        print("-Nadar")


class Walker:
    def __init__(self):
        self.walk = True
    def can_walk(self):
        print("-Caminar")


class Dog(Animal, Swimmer, Walker):
    
    name = 'Perro'
    def skills(self):
        super().can(self.name)
        super().can_walk()
        super().can_swim()


class Fish(Animal, Swimmer):
    
    name = 'Pez'
    def skills(self):
        super().can(self.name)
        super().can_swim()


class Bird(Animal, Flyer, Walker):
    
    name = 'Pajaro'
    def skills(self):
        super().can(self.name)
        super().can_walk()
        super().can_fly()


class Dock(Animal, Flyer, Swimmer, Walker):
    
    name = 'Pato'
    def skills(self):
        super().can(self.name)
        super().can_walk()
        super().can_swim()
        super().can_fly()

dog = Dog()
dog.skills()

fish = Fish()
fish.skills()

bird = Bird()
bird.skills()

dock = Dock()
dock.skills()



