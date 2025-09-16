import json


def read_json(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
        return data_json
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")


def print_base(data_pokemons):
    print("Resumen de Pokémones en el archivo JSON")
    for index in range(len(data_pokemons)):
        print(f"Nombre: {data_pokemons[index].get("name").get("english")}")
        print(f"   -Ataque: {data_pokemons[index].get("base").get("Attack")}")
        print(f"   -Defensa: {data_pokemons[index].get("base").get("Defense")}")
        print(f"   -Velocidad: {data_pokemons[index].get("base").get("Speed")}\n")


def main():
    path = "pokemons.json"
    data_pokemons = (read_json(path))
    print_base(data_pokemons)
    

if __name__ == "__main__":
    main()