import json


def read_json(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
        return data_json
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")


def find_pokemons(data_pokemons):
    find_pokemon = input("Ingrese el tipo de Pokémon que desea buscar: ").capitalize()
    pokemons_found = []
    for index in range(len(data_pokemons)):
        for item in data_pokemons[index].get("type"):
            if item == find_pokemon:
                pokemons_found.append(data_pokemons[index].get("name").get("english"))
    
    if pokemons_found == []:
        print ("No se encontro ningun Pokémon de ese tipo")
    else:
        print("Los Pokémones de ese tipo son:")
        for item in pokemons_found:
            print (f"\t-{item}")


def main():
    path = "pokemons.json"
    data_pokemons = (read_json(path))
    find_pokemons(data_pokemons)
    

if __name__ == "__main__":
    main()