def main():
    try:
        name = input("Ingrese su nombre: ")
        if name.isdigit():
            raise ValueError("El nombre no puede ser un número")
        try:
            age = int(input("Ingrese su edad: "))
        except ValueError:
            raise ValueError("Edad no valido")
        
    except Exception as ex:
        print(ex)
    
    else:
        print(f"Hola {name}, su edad es {age}")


if __name__ == "__main__":
    main()