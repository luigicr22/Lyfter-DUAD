from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        return area


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        perimeter = 2* (self.side + self.side)
        return perimeter
    
    def calculate_area(self):
        area = self.side * self.side
        return area


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        perimeter = 2* (self.length + self.width)
        return perimeter
    
    def calculate_area(self):
        area = self.length * self.width
        return area


circle = Circle(5)
print(f"Perimetro del circulo: {circle.calculate_perimeter():.2f}")
print(f"Area del circulo: {circle.calculate_area():.2f}\n")

square = Square(5)
print(f"Perimetro del cuadrado: {square.calculate_perimeter():.2f}")
print(f"Area del cuadrado: {square.calculate_area():.2f}\n")

rectangle = Rectangle(5,10)
print(f"Perimetro del rectangulo: {rectangle.calculate_perimeter():.2f}")
print(f"Area del rectangulo: {rectangle.calculate_area():.2f}")