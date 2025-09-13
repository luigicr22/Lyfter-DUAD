def reverse_string (string_to_reverse):
    string_reversed = ""
    for char in range (len(string_to_reverse)-1,-1,-1):
        string_reversed += string_to_reverse[char]
    return string_reversed


def main():
    print (reverse_string("Hola Mundo"))


if __name__ == "__main__":
  main()

