from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from app.utils import pokemon


def index(request, template_name="index.html"):
    context = {}
    return render(request, template_name, context)
    

def synchronous(request, template_name="_sync.html"):
    result, duration = pokemon.get_pokemon_sync()
    context = {
        'pokemons': result,
        'duration': duration,
    }
    return render(request, template_name, context)


async def asynchronous(request, template_name="_async.html"):
    context = {}
    return render(request, template_name, context)
