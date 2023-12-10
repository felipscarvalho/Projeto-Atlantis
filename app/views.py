from django.shortcuts import render
from .models import Species

# Create your views here.


def index(request):
    species = Species.objects.all().reverse()[0:3]

    return render(request, 'index.html', {'species': species})


def species(request):
    species = Species.objects.all().reverse()

    return render(request, 'species.html', {'species': species})
