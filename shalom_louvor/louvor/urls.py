from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todasMusicas', views.todasMusicas, name='todasMusicas' ),
    path('artista_id<int:artista_id>', views.todasMusicasArtista, name='todasMusicasArtista' ),
    path('buscar', views.buscar, name='buscar' ),
    path('<int:musica_id>', views.musica, name='musica'),
    path('musica/<int:musica_id', views.musica),
    path('dashboard', views.dashboard, name='dashboard'),
    
    
    path('criarMusica', views.criarMusica, name='criarMusica'),
    path('editarMusica/<int:musica_id>', views.editarMusica, name='editarMusica'),
    path('deletarMusica/<int:musica_id>', views.deletarMusica, name='deletarMusica'),
    path('atualizarMusica', views.atualizarMusica, name='atualizarMusica')
    
]
 

    