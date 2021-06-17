from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from app.utils import pokemon

import time


def index(request, template_name="index.html"):
    context = {}
    return render(request, template_name, context)
    

def synchronous(request, template_name="_sync.html"):
    start_time = time.time()
    result = pokemon.get_pokemon_sync()
    duration = time.time() - start_time

    context = {
        'pokemons': result,
        'duration': duration,
    }

    return render(request, template_name, context)


async def asynchronous(request, template_name="_async.html"):
    start_time = time.time()
    result = await pokemon.get_pokemon_async()
    duration = time.time() - start_time
    print(result)

    context = {
        'pokemons': result,
        'duration': duration,
    }

    return render(request, template_name, context)
