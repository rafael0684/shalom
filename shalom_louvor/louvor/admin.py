from django.contrib import admin
from .models import Musica

# Register your models here.

class ListandoMusica(admin.ModelAdmin):
    list_display = ('id', 'titulo_musica', 'nome_artista', 'release_year')
    list_display_links = ('id', "titulo_musica",'nome_artista', 'release_year')
    search_fields = ('id', "titulo_musica",'nome_artista', 'release_year','lyrics')
    list_filter= ('nome_artista', 'release_year')
    


admin.site.register(Musica, ListandoMusica)