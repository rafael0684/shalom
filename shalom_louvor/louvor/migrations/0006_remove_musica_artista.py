# Generated by Django 4.1 on 2022-08-26 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('louvor', '0005_musica_artista_musica_cover_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='artista',
        ),
    ]
