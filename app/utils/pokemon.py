import requests
import psycopg2
import aiohttp
import asyncio
import asyncpg

from django.conf import settings

import time

import logging
logger = logging.getLogger(__name__)


SQL_STATEMENT = "SELECT * FROM app_pokemon ORDER BY number;"
DB = settings.DATABASES['default']
CONNECTION_STRING = f'postgresql://{DB["USER"]}:{DB["PASSWORD"]}@{DB["HOST"]}:{DB["PORT"]}/{DB["NAME"]}'


def get_pokemon_sync():
    # Getting the Pokemon from DB without using the ORM
    # (for better comparision, because there is no async ORM yet)
    conn = psycopg2.connect(CONNECTION_STRING)
    cur = conn.cursor()
    cur.execute(SQL_STATEMENT)
    pokemons = cur.fetchmany(1000)

    cur.close()
    conn.close()

    return [{'number': pokemon[1], 'name': pokemon[2]} for pokemon in pokemons]


async def get_pokemon_async():
    conn = await asyncpg.connect(CONNECTION_STRING)
    async with conn.transaction():
        cur = await conn.cursor(SQL_STATEMENT)
        pokemons = await cur.fetch(1000)

    await conn.close()

    return [{'number': pokemon['number'], 'name': pokemon['name']} for pokemon in pokemons]
