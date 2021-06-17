from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

# Create your views here.

def index(request, template_name="index.html"):
    context = {}
    return render(request, template_name, context)
    
def synchronous(request, template_name="_sync.html"):
    context = {}
    return render(request, template_name, context)

def asynchronous(request, template_name="_async.html"):
    context = {}
    return render(request, template_name, context)
