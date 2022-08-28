from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs', views.songs, name='songs' ),
    path('buscar', views.buscar, name='buscar' ),
    path('<int:musica_id>', views.musica, name='musica'),
    path('musica/<int:musica_id', views.musica)
    
]
 

    