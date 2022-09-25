from django.contrib import admin
from .models import Playlist

class ListandoPlaylist(admin.ModelAdmin):
    list_display = ('id', 'playlist_name', 'playlist_data', 'playlist_createdDate')
    list_display_links = ('id', 'playlist_name', 'playlist_data', 'playlist_createdDate')
    search_fields = ('id', 'playlist_name', 'playlist_data', 'playlist_createdDate')
    list_filter= ('id', 'playlist_name', 'playlist_data', 'playlist_createdDate')
    


admin.site.register(Playlist, ListandoPlaylist)
