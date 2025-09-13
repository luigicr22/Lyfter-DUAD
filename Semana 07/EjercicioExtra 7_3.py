def sum_values(my_list):
    total_sum = 0.0
    for element in my_list:
        try:
            total_sum += float(element)
            print (f"\"{element}\" sumado correctamente") 
        
        except ValueError:
            print (f"Elemento inválido: {element}")
    
    print(f"Total de la suma: {total_sum}")

def main ():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    sum_values(my_list)

if __name__ == "__main__":
    main()