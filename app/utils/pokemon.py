import requests
import psycopg2
import aiohttp
import asyncio
import asyncpg

from django.conf import settings

import time

import logging
logger = logging.getLogger(__name__)

POKEMON_NUMBER = 25

SQL_STATEMENT = "SELECT * FROM app_pokemon ORDER BY number;"
SQL_STATEMENT_ONE = f"SELECT * FROM app_pokemon WHERE number = {POKEMON_NUMBER};"

DB = settings.DATABASES['default']
CONNECTION_STRING = f'postgresql://{DB["USER"]}:{DB["PASSWORD"]}@{DB["HOST"]}:{DB["PORT"]}/{DB["NAME"]}'


def get_pokemon_sync():
    # Getting the Pokemon from DB without using the Django ORM
    # (for better comparison, because there is no async ORM yet)
    conn = psycopg2.connect(CONNECTION_STRING)
    cur = conn.cursor()
    cur.execute(SQL_STATEMENT)
    pokemons = cur.fetchmany(1000)

    cur.close()
    conn.close()

    return [{'number': pokemon[1], 'name': pokemon[2]} for pokemon in pokemons]


def get_one_pokemon_sync():
    # Getting the Pokemon from DB without using the Django ORM
    # (for better comparison, because there is no async ORM yet)
    conn = psycopg2.connect(CONNECTION_STRING)
    cur = conn.cursor()
    cur.execute(SQL_STATEMENT_ONE)
    pokemon = cur.fetchone()

    cur.close()
    conn.close()

    return {
        'name': pokemon[2],
        'number': pokemon[1],
        'type1': pokemon[3],
        'type2': pokemon[4],
        'hp': pokemon[5],
        'attack': pokemon[6],
        'defense': pokemon[7],
        'sp_atk': pokemon[8],
        'sp_def': pokemon[9],
        'speed': pokemon[10],
        'generation': pokemon[11],
        'legendary': pokemon[12]
    }


async def get_pokemon_async():
    #print('get_pokemon_async 1')
    conn = await asyncpg.connect(CONNECTION_STRING)
    #print('get_pokemon_async 2')
    async with conn.transaction():
        #print('get_pokemon_async 3')
        cur = await conn.cursor(SQL_STATEMENT)
        #print('get_pokemon_async 4')
        pokemons = await cur.fetch(1000)

    #print('get_pokemon_async 5')
    await conn.close()

    return [{'number': pokemon['number'], 'name': pokemon['name']} for pokemon in pokemons]


async def get_one_pokemon_async():
    #print('one pokemon 1')
    conn = await asyncpg.connect(CONNECTION_STRING)
    #print('one pokemon ')
    async with conn.transaction():
        #print('one pokemon 3')
        cur = await conn.cursor(SQL_STATEMENT_ONE)
        #print('one pokemon 4')
        pokemon = await cur.fetchrow()

    #print('one pokemon 5')
    await conn.close()

    return pokemon
