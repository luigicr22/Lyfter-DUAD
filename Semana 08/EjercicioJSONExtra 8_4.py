import json


def read_json(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
        return data_json
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")


def average_for_type(data_pokemons):
    average_base_type = {}
    count_base_type = {}

    for index in range(len(data_pokemons)):
        pokemon_average = 0
        count_base = 0

        for value in data_pokemons[index].get("base").values():
            pokemon_average += value
            count_base += 1

        pokemon_average = int(pokemon_average/count_base)

        for value in data_pokemons[index].get("type"):
            if average_base_type.get(value) == None:
                average_base_type[value] = pokemon_average
                count_base_type[value] = 1

            else:
                average_base_type[value] += pokemon_average
                count_base_type[value] += 1

    print ("Lista de Pokémon por tipo y promedio de nivel")
    for type, sum in average_base_type.items():
        print(f"Pokémons {type}:")
        print(f"  -Cantidad de Pokémons: {count_base_type.get(type)}")
        print(f"  -Promedio de nivel: {int(sum/count_base_type.get(type))}\n")


def main():
    path = "pokemons.json"
    data_pokemons = (read_json(path))
    average_for_type(data_pokemons)

if __name__ == "__main__":
    main()