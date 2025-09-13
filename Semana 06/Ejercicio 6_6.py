def sort_string(string_original):
    print(f"String original= {string_original}")

    list_original = convert_to_list (string_original)
    print(f"Lista original= {list_original}")

    list_sorted = sort_list(list_original)
    print(f"Lista ordenada= {list_sorted}")

    string_sorted = convert_to_string(list_sorted)
    return string_sorted


def convert_to_list(string_original):
    list_original = string_original.split("-")
    return (list_original)
    

def sort_list(list_original):
    list_original.sort()
    return (list_original)


def convert_to_string(list_sorted):
    string_sorted = ""
    for index in range(len(list_sorted)):
        string_sorted += list_sorted[index]
        if index < (len(list_sorted)-1):
            string_sorted += "-"
    return string_sorted


def main():
    string_original = "python-variable-funcion-computadora-monitor"
    print (f"String ordenado= {sort_string(string_original)}")


if __name__ == "__main__":
  main()

