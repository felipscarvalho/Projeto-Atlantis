from django.db import models

# Create your models here.


class StatusOptions(models.IntegerChoices):
    extinct = 0, 'Extinto'
    threatened_with_extinction = 1, 'Ameaçado de Extinção'


class Species(models.Model):
    image = models.ImageField(upload_to='animals/',
                              default='defaults/animal_default.png')
    name = models.CharField(max_length=255, verbose_name='Nome')
    scientific_name = models.CharField(
        max_length=255, verbose_name='Nome Científico')
    status = models.IntegerField(
        choices=StatusOptions.choices, verbose_name='Status')
    description = models.TextField(verbose_name='Descrição')
