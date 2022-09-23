from gc import get_objects
from mailbox import NotEmptyError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Musica, Artista
from django.contrib.auth.models import User



def index(request):
    '''Rederiza a pagina Index do site'''
    musicas = Musica.objects.order_by('-data_musica').all
    artistas= Artista.objects.order_by('-nome_artista').all

    dados = {
        'musicas' : musicas,
        'artistas': artistas
    }
    return render(request, 'index.html', dados)

def buscar(request):
    '''Busca em Titulo e Letras de musicas'''
    
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

def todasMusicas(request):
    '''Mostra todas as musicas por ordem alfabetica'''
    musicas = Musica.objects.order_by('titulo_musica').all
    dados = {
        'musicas' : musicas
    }
    return render(request, 'todasMusicas.html', dados)

def todasMusicasArtista(request, artista_id):
    '''Mostra todas as musicas de um artista por ordem alfabetica'''
    artista = get_object_or_404(Artista, pk =artista_id)
    musicas = Musica.objects.order_by('-data_musica')
    musicas_artista = musicas.filter(nome_artista = artista)

    dados = {
        'musicas' : musicas_artista,
    }

    return render(request, 'todasMusicas.html', dados)
    

def musica(request, musica_id):
    '''Visualizacao detalhes da musica requerida'''
    musica = get_object_or_404(Musica, pk=musica_id)
    musica_estrofes = musica.lyrics.split("£")
    
    musica_a_exibir = {
        'musica': musica,
        'musica_estrofes': musica_estrofes
    }
    
    return render(request, 'musica.html', musica_a_exibir)


def dashboard(request):
    ''' Lista de musicas criadas por Usuario Logado'''
    lista_musicas = Musica.objects.order_by('-data_musica')
    user= get_object_or_404(User, pk=request.user.id)
    musicas = lista_musicas.filter(user=user)
    dados = {
        'musicas' : musicas
    }
    
    return render(request, 'dashboard.html', dados)

def criarMusica(request):
    '''Formulario para adicionar nova musica'''
    artistas = Artista.objects.order_by('nome_artista')
    dados = {
        'artistas': artistas,    
    }
    

    if request.method == 'POST':
        titulo_musica = request.POST['titulo_musica'].strip()
        input_artista = request.POST['nome_artista']
        nome_artista = buscar_ou_criar_artista(input_artista)
        release_year = request.POST['release_year']
        lyrics = request.POST['lyrics']
        chords =request.POST['chords']
        user = get_object_or_404(User, pk=request.user.id)
        nova_musica = Musica.objects.create(titulo_musica=titulo_musica, 
                                            nome_artista=nome_artista,
                                            release_year=release_year,
                                            lyrics=lyrics,
                                            chords=chords,
                                            user=user)
        nova_musica.save()
        messages.success(request, "Musica adicionada com sucesso")
        
        return redirect('dashboard')
    
    return render(request, 'criarMusica.html', dados)

def buscar_ou_criar_artista(input_artista):
    '''Metodo busca por artista no DB / devolve Artista ou cria novo artista'''
    if Artista.objects.filter(nome_artista = input_artista).exists():
        artista = get_object_or_404(Artista, nome_artista=input_artista)
        return artista
    else:
        artista = Artista.objects.create(nome_artista=input_artista.strip())
        artista.save()
        return artista

def editarMusica(request, musica_id):
    '''Formulario para editar musica'''
    musica = get_object_or_404(Musica, pk=musica_id)
    musica_a_editar = {'musica': musica }

    return render(request, 'editarMusica.html', musica_a_editar)

def atualizarMusica(request):
    '''Efetua atualizacoes nos atributos de uma musica'''
    if request.method == 'POST':
        musica_id = request.POST['musica_id']
        m = Musica.objects.get(pk=musica_id)
        m.titulo_musica = request.POST['titulo_musica'].strip()
        input_artista = request.POST['input_artista']
        m.nome_artista = buscar_ou_criar_artista(input_artista)
        m.release_year = request.POST['release_year']
        m.lyrics = request.POST['lyrics']
        m.chords = request.POST['chords']
        m.save()

        messages.success(request, 'Musica atualizada com sucesso')

        return redirect('dashboard')

def deletarMusica(request, musica_id):
    '''Deleta musica'''
    musica_a_deletar = get_object_or_404(Musica, pk=musica_id)
    musica_a_deletar.delete()
    
    messages.success(request, "Musica deletada com sucesso")

    return redirect('dashboard')



