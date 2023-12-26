from django.shortcuts import render
from .models import Species, Disasters, Organizations

# Create your views here.


def index(request):
    species = Species.objects.all().reverse()[0:3]
    disasters = Disasters.objects.all().reverse()[0:3]
    contribution = Organizations.objects.all()

    return render(request, 'index.html', {'species': species, 'disasters': disasters, 'contributions': contribution})


def species(request):
    species = Species.objects.all().reverse()
    disasters = Disasters.objects.all().reverse()

    return render(request, 'species.html', {'species': species, 'disasters': disasters})


def aboutus(request):
    return render(request, 'aboutus.html')
