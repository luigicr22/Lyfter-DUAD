import json


def read_json(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
        return data_json
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")


def print_pokemons(data_pokemons):
    print("Lista de Pokémones:\n")
    for index in range(len(data_pokemons)):
        print(f"Nombre: {data_pokemons[index].get("name").get("english")}")
        print(f"\tTipo:")
        for item in data_pokemons[index].get("type"):
            print(f"\t  -{item}")
        print(f"\tBase:")
        for base, value in data_pokemons[index].get("base").items():
            print(f"\t  -{base}= {value}")
        print("\n")


def main():
    path = "pokemons.json"
    data_pokemons = (read_json(path))
    print_pokemons(data_pokemons)
    

if __name__ == "__main__":
    main()