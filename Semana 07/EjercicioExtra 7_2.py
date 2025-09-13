def convert_to_int(list_string):
    print("Resultado:")
    for element in list_string:
        try:
            print (f"\"{element}\" convertido a: {int(element)}") 
        
        except ValueError:
            print (f"No se pudo convertir el elemento: {element}")
        

def main ():
    my_list = ['4', 'hola', '10', '5.2']
    convert_to_int(my_list)

if __name__ == "__main__":
    main()