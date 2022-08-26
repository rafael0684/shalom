from email.charset import Charset
from platform import release
from statistics import mode
from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from datetime import datetime
from artista.models import Artista



# Create your models here.
class Musica(models.Model):
    titulo_musica = models.CharField(max_length=200)
    nome_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    release_year = models.IntegerField()
    lyrics = models.TextField()
    data_musica = models.DateField(default=datetime.now, blank=True)
    
    


