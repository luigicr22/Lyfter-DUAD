import csv

def input_game ():
    list_games = []
    game  = {}

    while True:
        print ("NUEVO INGRESO")
        game["Nombre"] = input ("Ingrese el nombre del videojuego: ")
        game["Género"] = input ("Ingrese el Género del videojuego: ")
        game["Desarrollador"] = input ("Ingrese el Desarrollador del videojuego: ")
        game["Clasificación ESRB"] = input ("Ingrese la Clasificación ESRB del videojuego: ")
        list_games.append(game.copy())
        other_game = input ("Presione \"N\" si desea dejar de agregar videojuegos o otra tecla si desea continuar agregando: ")
        if other_game == "N":
            break
    
    return (list_games)
    

def create_csv (path, data, headers):
    with open(path, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


def main ():
    list_games = input_game()
    create_csv ("videogamesAlternative.csv", list_games, list_games[0].keys())
    print ("Archivo CSV alternativo creado")


if __name__ == "__main__":
    main()
