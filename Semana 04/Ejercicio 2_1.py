#Ejercicio 2.1
#Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#   1. Si el precio es menor a 100, el descuento es del 2%.
#   2. Si el precio es mayor o igual a 100, el descuento es del 10%.

price = int(input("Ingrese el presio del producto: "))
if (price < 100):
    final_price = price - (price * 0.02)
else:
    final_price = price - (price * 0.1)

print(f"El precio final del producto es: {final_price}")
