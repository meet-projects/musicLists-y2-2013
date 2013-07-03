from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
	return self.name
   
class Artist(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Album(models.Model):
    name=models.CharField(max_length=200)
    artist=models.ForeignKey('Artist')
    genres=models.ManyToManyField('Genre')
    def __unicode__(self):
	return self.name

class Song(models.Model):
    name=models.CharField(max_length=200)
    artist=models.ForeignKey('Artist')
    genres=models.ManyToManyField('Genre')
    album=models.ForeignKey('Album')
    link=models.CharField(max_length=2000)
    def __unicode__(self):
        return self.name

class Guy(models.Model):
    user=models.OneToOneField(User)
    favsongs=models.ManyToManyField('Song')
    favartists=models.ManyToManyField('Artist')
    favgenres=models.ManyToManyField('Genre')
    def __unicode__(self):
        return self.user.username

    @staticmethod
    def make_default(user):
        try:
          genre = Genre.objects.filter(name='empty')[0]
        except IndexError:
          genre = Genre(name='empty')
          genre.save()
        try:
          artist = Artist.objects.filter(name='empty')[0]
        except IndexError:
          artist = Artist(name='empty')
          artist.save()
        try:
          song = Song.objects.filter(name='empty')[0]
        except IndexError:
          try:
            album = Album.objects.filter(name='empty')[0]
          except IndexError:
            album = Album(name='empty', artist=artist)
            album.save()
            album.genres.add(genre)
            
          song = Song(name='empty', artist=artist, album=album, link='youtube.com')
          song.save()
          song.genres.add(genre)
          song.save()
        guy = Guy(user=user)
        guy.save()
        guy.favsongs.add(song)
        guy.favartists.add(artist)
        guy.favgenres.add(genre)
        guy.save()
        return guy
