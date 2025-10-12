class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    

class Inventory:
    inventory = []

    def add_product(self,product):
        self.inventory.append(product)
    
    def list_inventory(self):
        for item in self.inventory:
            print(f"Producto: {item.name}")
            print(f"   Precio: {item.price}")
            print(f"   Cantidad: {item.quantity}\n")

    def calc_inventory(self):
        total = 0
        for item in self.inventory:
            total += (item.price * item.quantity)
        print(f"El valor total del inventario es: {total}")

product1 = Product("Mouse",5000,3)
product2 = Product("Teclado",8000,2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.list_inventory()
inventory.calc_inventory()

