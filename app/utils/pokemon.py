import requests
import time

MAX_POKEMON = 151
NUM_OF_POKEMON_TO_GET = 10

def get_pokemon_sync():
    start_time = time.time()

    pokemons = []

    for number in range(1, NUM_OF_POKEMON_TO_GET + 1):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon['name'])
        pokemons.append(pokemon['name'])

    end_time = time.time() - start_time

    return pokemons, end_time