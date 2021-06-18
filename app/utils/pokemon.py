import requests
import aiohttp
import asyncio

import time

import logging
logger = logging.getLogger(__name__)


MAX_POKEMON = 50
NUM_OF_POKEMON_TO_GET = None or MAX_POKEMON

#POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
POKE_API_URL = 'https://en.wikipedia.org/w/api.php?format=json&action=query&titles=pokemon'


def get_pokemon_sync():
    pokemons = []
    for number in range(1, NUM_OF_POKEMON_TO_GET+1):
        time.sleep(0.1)
        logger.debug(number)
        pokemons.append('x')

    return pokemons 

async def async_sleep(number):
    await asyncio.sleep(0.1)
    logger.debug(number)    
    return 'x'

async def get_pokemon_async():
    pokemons, _ = await asyncio.wait(
        [async_sleep(number) for number in range(1, NUM_OF_POKEMON_TO_GET+1)]
    )   
    return [ pokemon.result for pokemon in pokemons]
