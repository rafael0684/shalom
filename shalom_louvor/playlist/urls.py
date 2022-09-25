from django.urls import path
from . import views

urlpatterns = [
    path('criarPlaylist', views.criarPlaylist, name='criarPlaylist'),
    path('add_M_Playlist<playlist_id', views.add_M_Playlist, name='add_M_Playlist'),
    path('playlist_id<int:playlist_id>', views.add_M_Playlist, name='add_M_Playlist' ),
    path('atualizarPlaylist', views.atualizarPlaylist, name='atualizarPlaylist'),
    path('deletarPlaylist/<int:playlist_id>', views.deletarPlaylist, name='deletarPlaylist'),
    path('deletar_M_Playlist<int:playlist_id>/<int:musica_id>', views.deletar_M_Playlist, name='deletar_M_Playlist')
]   