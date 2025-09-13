products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

for_category = {}

for index_product in range(len(products)):
    if (products[index_product]["category"] in for_category):
        for_category[products[index_product]["category"]] += products[index_product]["price"]
    else:
        for_category[products[index_product]["category"]] = products[index_product]["price"]

print(for_category)