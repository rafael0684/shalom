from django.db import models

# Create your models here.
class Artista(models.Model):
    nome_artista = models.CharField(max_length=200)
    artista_pic = models.ImageField(blank=True, upload_to='cover_pic')
    
    def __str__(self) -> str:
        return self.nome_artista

