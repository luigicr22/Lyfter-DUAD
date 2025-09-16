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


def count_gender (list_games):
    count_gender = {}
    for index in range(len(list_games)):
        if count_gender.get(list_games[index].get("Género")) == None:
            count_gender[list_games[index].get("Género")] = 1
        else:
            count_gender[list_games[index].get("Género")] += 1
    
    print ("Géneros encontrados:\n")
    for gender, number in count_gender.items():
        print(f"{gender}= {number}") 


def main():
    list_games = read_csv("videogames.csv")
    count_gender (list_games)


if __name__ == "__main__":
    main()