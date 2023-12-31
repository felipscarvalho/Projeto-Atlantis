# Generated by Django 4.2.7 on 2023-12-15 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_disasters_alter_species_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='disasters/')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=512)),
                ('description', models.TextField()),
            ],
        ),
    ]
