import csv

def read_csv (path):
    list_games = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader (file)
            for row in reader:
                list_games.append(row)
        return list_games
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")
        exit()



def print_games (list_games):
    print ("Lista de videojuegos en el archivo CSV")
    for index in range(len(list_games)):
        print (f"\n{index+1}° Juego:")
        print(f"Nombre: {list_games[index].get("Nombre")}")
        print(f"Género: {list_games[index].get("Género")}")
        print(f"Desarrollador: {list_games[index].get("Desarrollador")}")
        print(f"Clasificación ESRB: {list_games[index].get("Clasificación ESRB")}")


def main():
    list_games = read_csv("videogames.csv")
    print_games(list_games)


if __name__ == "__main__":
    main()
