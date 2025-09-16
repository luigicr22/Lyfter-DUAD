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


def search_developer (list_games):
    developer = input ("Que desarrollados de videojuegos desea buscar: ")
    print(f"Videojuegos desarrollados por {developer}\n")
    count_games = 0

    for index in range(len(list_games)):
        if list_games[index].get("Desarrollador") == developer:
            count_games += 1
            print (f"{count_games}){list_games[index].get("Nombre")}")
            print (f"\t-Género: {list_games[index].get("Género")}")
            print (f"\t-Clasificación ESRB: {list_games[index].get("Clasificación ESRB")}:")
    
    if count_games == 0:
        print (f"No hay videojuegos en el archivo CSV desarrollados por {developer}\n")


def main():
    list_games = read_csv("videogames.csv")
    search_developer (list_games)


if __name__ == "__main__":
    main()
