import requests
import aiohttp


MAX_POKEMON = 151
NUM_OF_POKEMON_TO_GET = None or MAX_POKEMON

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'


def get_pokemon_sync():
    pokemons = []

    for number in range(1, NUM_OF_POKEMON_TO_GET+1):
        pokemon_url = f'{POKE_API_URL}{number}'
        resp = requests.get(pokemon_url)
        pokemon = resp.json()
        print(pokemon['name'])
        pokemons.append(pokemon['name'])

    return pokemons


async def get_pokemon_async():
    pokemons = []

    async with aiohttp.ClientSession() as session:
        for number in range(1, NUM_OF_POKEMON_TO_GET+1):
            pokemon_url = f'{POKE_API_URL}{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])
                pokemons.append(pokemon['name'])

    return pokemons