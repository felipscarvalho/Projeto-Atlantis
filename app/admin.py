from django.contrib import admin
from .models import Species

# Register your models here.


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'scientific_name', 'status']


admin.site.register(Species, SpeciesAdmin)
