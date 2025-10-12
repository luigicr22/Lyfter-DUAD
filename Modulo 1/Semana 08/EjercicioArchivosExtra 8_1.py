def read_file (path):
    string = ""
    try:
        with open (path) as file:
            print("OLD FILE")
            print(file.read())
            file.seek(0)
            for line in file.read():
                string += line
        
            new_string = string.replace("\n"," ")

        with open ("new_hola_mundo.txt", "w", encoding='utf-8') as file:
            file.write(new_string)
        
        return "new_hola_mundo.txt"
    
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")
        exit()


def main ():
    new_path = read_file ("hola_mundo.txt")

    print("\nNEW FILE")
    with open (new_path) as file:
        print(file.read())


if __name__=="__main__":
    main()

