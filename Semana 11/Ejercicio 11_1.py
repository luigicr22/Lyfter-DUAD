import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def get_area(self):
        print(f"Area del circulo: {math.pi * self.radius * self.radius}")


circle1 = Circle(5)
circle1.get_area()

