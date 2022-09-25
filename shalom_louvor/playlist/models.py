from datetime import datetime
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from louvor.models import Musica

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100, default=datetime.now)
    playlist_data = models.DateField(default=datetime.now, blank=True)
    playlist_musicas = models.ManyToManyField(Musica, blank=True)

    playlist_createdDate = models.DateField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete= models.SET_DEFAULT, default=1)
    def __str__(self) -> str:
        return self.playlist_name