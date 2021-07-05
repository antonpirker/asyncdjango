from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from app.utils import pokemon

import time

import logging
logger = logging.getLogger(__name__)


def index(request, template_name="index.html"):
    context = {}
    return render(request, template_name, context)


def synchronous(request, template_name="_sync.html"):
    start_time = time.time()
    logger.warn('sync 1')
    result = pokemon.get_pokemon_sync()
    logger.warn('sync 2')
    pikachu = pokemon.get_one_pokemon_sync()
    logger.warn('sync 3')
    duration = time.time() - start_time


    context = {
        'pokemon': pikachu,
        'pokemons': result,
        'duration': duration,
    }

    return render(request, template_name, context)


async def asynchronous(request, template_name="_async.html"):
    start_time = time.time()
    logger.warn('async 1')
    result = await pokemon.get_pokemon_async()
    logger.warn('async 2')
    pikachu = await pokemon.get_one_pokemon_async()
    logger.warn('async 3')
    duration = time.time() - start_time
    
    context = {
        'pokemon': pikachu,
        'pokemons': result,
        'duration': duration,
    }

    return render(request, template_name, context)
