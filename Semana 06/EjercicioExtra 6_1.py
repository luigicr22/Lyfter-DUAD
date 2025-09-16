def count_char (original_string, char_to_find):
    count = str(original_string).count(char_to_find)
    return count


def main():
    original_string = input("Ingrese un texto: ")
    char_to_find = input("ingrese el caracter que desea buscar: ")
    print (f"Se a encontrado el caracter \"{char_to_find}\" {count_char(original_string,char_to_find)} veces")


if __name__ == "__main__":
    main()