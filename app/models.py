from django.db import models

# Create your models here.


class StatusOptions(models.IntegerChoices):
    extinct = 0, 'Extinto'
    threatened_with_extinction = 1, 'Ameaçado de Extinção'


class Species(models.Model):
    image = models.ImageField(upload_to='animals/',
                              default='defaults/animal_default.jpg')
    name = models.CharField(max_length=255, verbose_name='Nome')
    scientific_name = models.CharField(
        max_length=255, verbose_name='Nome Científico')
    status = models.IntegerField(
        choices=StatusOptions.choices, verbose_name='Status')
    description = models.TextField(verbose_name='Descrição')


class Disasters(models.Model):
    image = models.ImageField(upload_to='disasters/')
    title = models.CharField(max_length=255)
    description = models.TextField()


class Organizations(models.Model):
    image = models.ImageField(upload_to='disasters/')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=512)
    instagram = models.CharField(max_length=512)
    instagram_link = models.CharField(max_length=512)
    description = models.TextField()
