def add_text (path, alert):
    string = input("Ingrese una línea de texto: ")+"\n"
    with open(path, "a", encoding='utf-8') as file:
        file.write(string)

    print (alert)

def main ():
    try:
        with open ("add_text.txt") as file:
            print("OLD FILE")
            print(file.read())
            new_path = add_text ("add_text.txt", "El texto se agrega al final del archivo sin borrar lo anterior")
    except FileNotFoundError:
        new_path = add_text ("add_text.txt", "El archivo fue creado y se agrego la linea")
    
    print("\nNEW FILE")
    with open ("add_text.txt") as file:
        print(file.read())

if __name__=="__main__":
    main()