# Generated by Django 4.1 on 2022-09-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('louvor', '0009_alter_musica_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='chords',
            field=models.TextField(blank=True),
        ),
    ]
