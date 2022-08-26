from django.contrib import admin
from .models import    Artista

# Register your models here.
class ListandoArtistas(admin.ModelAdmin):
    list_display = ('id', 'nome_artista',)
    list_display_links = ( "nome_artista",)
    search_fields = ('id', "nome__artista",)
    list_filter= ('nome_artista',)
    


admin.site.register(Artista, ListandoArtistas)