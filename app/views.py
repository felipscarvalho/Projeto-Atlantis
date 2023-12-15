from django.shortcuts import render
from .models import Species, Disasters

# Create your views here.


def index(request):
    species = Species.objects.all().reverse()[0:3]
    disasters = Disasters.objects.all().reverse()[0:3]

    return render(request, 'index.html', {'species': species, 'disasters': disasters})


def species(request):
    species = Species.objects.all().reverse()

    return render(request, 'species.html', {'species': species})


def aboutus(request):
    return render(request, 'aboutus.html')
