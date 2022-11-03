from django.db import models

# Create your models here.
class  Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()

class  Song(models.Model):
    # artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField(max_length=100)
    likes = models.CharField(max_length=700)
    artiste_id = models.CharField(max_length=250)


class Lyric(models.Model):
    # song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    song_id = models.CharField(max_length=300)
