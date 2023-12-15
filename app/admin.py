from django.contrib import admin
from .models import Species, Disasters, Organizations

# Register your models here.


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'scientific_name', 'status']


class DisastersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'instagram',
                    'instagram_link', 'title', 'description']


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Disasters, DisastersAdmin)
admin.site.register(Organizations, OrganizationsAdmin)
