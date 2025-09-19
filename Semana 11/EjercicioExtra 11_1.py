class Rectangle:
    def __init__(self):
        try:
            width = int(input("Ingrese el ancho: "))
            height = int(input("Ingrese la altura: "))
            
            if width > 0 and height > 0:
                self.width = width
                self.height = height
                self.created = True
            else:
                print("Existe un valor negativo o 0, los valores deben ser positivos")
                self.created = False
        except ValueError:
            print("Solo se aceptan números para la altura y ancho del rectangulo")
            self.created = False

    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_perimeter(self):
        perimeter = self.height + self.height + self.width + self.width
        return perimeter

rectangle1 = Rectangle()
if rectangle1.created:
    print(f"El area del rectangulo es: {rectangle1.get_area()}")
    print(f"El perimetro del rectangulo es: {rectangle1.get_perimeter()}")