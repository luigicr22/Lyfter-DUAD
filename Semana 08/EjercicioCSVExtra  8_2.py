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


def search_games(list_games):
    search_esrb = input ("Que clasificacion desea buscar: ")
    print (f"Lista de videojuegos en el archivo CSV con clasificacion {search_esrb}\n")
    count_games = 0
    for index in range(len(list_games)):
        if list_games[index].get("Clasificación ESRB") == search_esrb:
            print(f"Nombre: {list_games[index].get("Nombre")}")
            print(f"Género: {list_games[index].get("Género")}")
            print(f"Desarrollador: {list_games[index].get("Desarrollador")}")
            print(f"Clasificación ESRB: {list_games[index].get("Clasificación ESRB")}\n")
            count_games += 1
    
    if count_games == 0:
        print (f"No hay videojuegos en el archivo CSV con clasificacion {search_esrb}\n")
    

def main():
    list_games = read_csv("videogames.csv")
    search_games(list_games)


if __name__ == "__main__":
    main()