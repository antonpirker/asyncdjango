import requests
import psycopg2
import aiohttp
import asyncio

from django.conf import settings

import time

import logging
logger = logging.getLogger(__name__)

def get_pokemon_sync():
    # Getting the Pokemon from DB without using the ORM
    # (for better comparision, because there is no async ORM yet)
    db_settings = settings.DATABASES['default']
    connection_string = f'postgresql://{db_settings["USER"]}:{db_settings["PASSWORD"]}@{db_settings["HOST"]}:{db_settings["PORT"]}/{db_settings["NAME"]}'

    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM app_pokemon;")
    pokemons = cur.fetchall()

    return pokemons 


async def get_pokemon_async():

    async with aiohttp.ClientSession() as session:
        async with session.get(POKEMON_URL) as resp:
            pokemon = await resp.read()
            print(pokemon)


    """
    pokemons, _ = await asyncio.wait(
        [async_sleep(number) for number in range(1, NUM_OF_POKEMON_TO_GET+1)]
    )   
    return [ pokemon.result for pokemon in pokemons]
    """