from gc import get_objects
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Musica


def index(request):
    musicas = Musica.objects.order_by('-data_musica').all
    dados = {
        'musicas' : musicas
    }
    return render(request, 'index.html', dados)

def songs(request):
    musicas = Musica.objects.order_by('titulo_musica').all
    dados = {
        'musicas' : musicas
    }
    return render(request, 'songs.html', dados)


def musica(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)

    musica_a_exibir = {
        'musica': musica
    }
    
    return render(request, 'musica.html', musica_a_exibir )

def buscar(request):
    
    lista_musicas = Musica.objects.order_by('-data_musica')
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_de_musicas = lista_musicas.filter(titulo_musica__icontains=nome_a_buscar)
            lista_lyrics = lista_musicas.filter(lyrics__icontains=nome_a_buscar)
            dados = {
                'musicas' : lista_de_musicas,
                'musicas' : lista_lyrics,
            }

    return render(request, 'buscar.html', dados)