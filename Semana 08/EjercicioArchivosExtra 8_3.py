def convert_uppercase (path):
    string = ""
    try:
        with open (path) as file:
            print("OLD FILE")
            print(file.read())
            file.seek(0)
            for line in file.readlines():
                string += line.upper()
            
        with open("upper.txt", "w", encoding='utf-8') as file:
            file.write(string)

        return "upper.txt"

    except FileNotFoundError:
        print("No se encuentra archivo para cargar")
        exit()


def main ():
    new_path = convert_uppercase ("lower.txt")

    print("\nNEW FILE")
    with open (new_path) as file:
        print(file.read())

if __name__=="__main__":
    main()