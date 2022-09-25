from audioop import add
from datetime import datetime
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Musica, Playlist
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User

def criarPlaylist(request):
    
    if request.method == 'POST':
        playlist_name = request.POST['playlist_name'].strip()
        playlist_data = request.POST['playlist_data']
        user = get_object_or_404(User, pk=request.user.id)
        nova_playlist = Playlist.objects.create(playlist_name=playlist_name,
                                                playlist_data=playlist_data,
                                                user=user)
        nova_playlist.save()
        messages.success(request, "Nova Playlist adicionada")

        return redirect('add_M_Playlist', nova_playlist.id)

    return render(request, 'criarPlaylist.html')



def add_M_Playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk= playlist_id)
    musicas = Musica.objects.order_by('-data_musica')
    contexto = {
        'playlist': playlist,
        'musicas': musicas,
    }
    return render(request, 'addMusica_Playlist.html', contexto)
    
def atualizarPlaylist(request):
    
    if request.method == 'POST':
        playlist_id = request.POST['playlist_id']
        playlist = get_object_or_404(Playlist, pk= playlist_id)
        musica_a_add = request.POST['titulo_musica']
        m =get_object_or_404(Musica, titulo_musica=musica_a_add)
        
        playlist.playlist_musicas.add(m)
        
        playlist.save()
        messages.success(request,'Musica adicionada a playlist')
        
        return redirect('add_M_Playlist', playlist.id)

def deletar_M_Playlist(request, playlist_id, musica_id):
    print(playlist_id)
    print(musica_id)
    playlist= get_object_or_404(Playlist, pk=playlist_id)
    musica_a_del = get_object_or_404(Musica, pk=musica_id)
    playlist.playlist_musicas.remove(musica_a_del) 

    return redirect('add_M_Playlist', playlist_id)

def deletarPlaylist(request, playlist_id):
    '''Deleta playlist'''
    playlist_a_deletar = get_object_or_404(Playlist, pk=playlist_id)
    playlist_a_deletar.delete()
    
    messages.success(request, "Playlist deletada com sucesso")

    return redirect('dashboard')

    