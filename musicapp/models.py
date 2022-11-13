from django.db import models

# Create your models here.
class  Artiste(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()

    def __str__ (self):
        return self.first_name + '-' + self.last_name

class  Song(models.Model):
    # artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField(max_length=100)
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

    def __str__ (self):
        return self.title


class Lyric(models.Model):
    # song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    song_id = models.IntegerField()

    def __str__ (self):
        return self.content
