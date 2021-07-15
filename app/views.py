from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from app.utils import pokemon

import asyncio
import time

import logging
logger = logging.getLogger(__name__)


def index(request, template_name="index.html"):
    context = {}
    return render(request, template_name, context)


def synchronous(request, template_name="_sync.html"):
    start_time = time.time()
    result = pokemon.get_pokemon_sync()
    pikachu = pokemon.get_one_pokemon_sync()
    duration = time.time() - start_time

    context = {
        'pokemon': pikachu,
        'pokemons': result,
        'duration': duration,
    }

    return render(request, template_name, context)


async def asynchronous(request, template_name="_async.html"):
    start_time = time.time()
    results = await asyncio.gather(
        pokemon.get_one_pokemon_async(),
        pokemon.get_pokemon_async(),
    )
    pikachu = results[0]
    result = results[1]
    duration = time.time() - start_time

    context = {
        'pokemon': pikachu,
        'pokemons': result,
        'duration': duration,
    }

    return render(request, template_name, context)
