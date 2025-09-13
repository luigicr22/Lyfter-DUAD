import json
import os

def read_json(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            data_json = json.load(file)
        return data_json
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")


def write_json(path,data_json):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, indent=4)
    print("Pokemon guardado en el archivo JSON")


def add_json(data_pokemons):
    while True:
        try: 
            name_pokemon = input("Ingrese el nombre en ingles del pokemon: ")
            type_pokemon = input("Ingrese el tipo de pokemon: ")
            base_hp_pokemon = int(input("Ingrese el el valor de HP del pokemon: "))
            base_attack_pokemon = int(input("Ingrese el el valor de Attack del pokemon: "))
            base_defense_pokemon = int(input("Ingrese el el valor de Defense del pokemon: "))
            base_spattack_pokemon = int(input("Ingrese el el valor de Sp. Attack del pokemon: "))
            base_spdefensehp_pokemon = int(input("Ingrese el el valor de Sp. Defense del pokemon: "))
            base_speed_pokemon = int(input("Ingrese el el valor de Speed del pokemon: "))
            break
        except ValueError:
            os.system("cls")
            print("Ingrese valores numerales en los rangos base")

    new_pokemon = {
        "name": {
            "english": name_pokemon
        },
        "type": [
            type_pokemon
        ],
        "base": {
            "HP": base_hp_pokemon,
            "Attack": base_attack_pokemon,
            "Defense": base_defense_pokemon,
            "Sp. Attack": base_spattack_pokemon,
            "Sp. Defense": base_spdefensehp_pokemon,
            "Speed": base_speed_pokemon
        }
    }
    data_pokemons.append(new_pokemon)
    return data_pokemons


def main():
    path = "pokemons.json"
    data_pokemons = (read_json(path))
    data_pokemons = add_json(data_pokemons)
    write_json(path,data_pokemons)
    

if __name__ == "__main__":
    main()