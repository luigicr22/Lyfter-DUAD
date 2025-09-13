def is_len_than (original_list,len_than):
    list_len_than = []
    for string in original_list:
        if len(string) > len_than:
            list_len_than.append(string)
    return (list_len_than)


def convert_to_list(string_original):
    list_original = string_original.split("-")
    return (list_original)


def main ():
    original_list = convert_to_list(input("Ingrese la lista de palabras separada por un \"-\" (Ejemplo: carro-casa): "))
    len_than = int(input("Ingrese el numero de letras minimas en la palabra: "))
    print (f"La lista original es: {original_list}")
    print (f"La lista con palabras mas largas que {len_than} caracteres es: {is_len_than(original_list,len_than)}")


if __name__ == "__main__":
    main()