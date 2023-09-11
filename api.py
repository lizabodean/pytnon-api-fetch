import requests

def get_generation_pokemon(generation_id):
    url = f'https://pokeapi.co/api/v2/generation/{generation_id}/'
    response = requests.get(url)

    if response.ok:
        data = response.json()
        pokemon_list = []

        for pokemon in data['pokemon_species']:
            pokemon_name = pokemon['name']
            pokemon_list.append(pokemon_name)

        return pokemon_list
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
        return []

generation_id = 3
pokemon_list = get_generation_pokemon(generation_id)

if pokemon_list:
    print(f"Pokemon in Generation {generation_id}:")
    for pokemon_name in pokemon_list:
        print(pokemon_name)