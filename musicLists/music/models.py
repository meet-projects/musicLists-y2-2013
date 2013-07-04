from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

    @staticmethod
    def get_default():
        try:
            genre = Genre.objects.filter(name='empty')[0]
        except IndexError:
            genre = Genre(name='empty')
            genre.save()
        return genre
   
class Artist(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

    @staticmethod
    def get_default():
        try:
            artist = Artist.objects.filter(name='empty')[0]
        except IndexError:
            artist = Artist(name='empty')
            artist.save()
        return artist

class Album(models.Model):
    name=models.CharField(max_length=200)
    artist=models.ForeignKey('Artist')
    genres=models.ManyToManyField('Genre')
    def __unicode__(self):
        return self.name

    @staticmethod
    def get_default():
        try:
            album = Album.objects.filter(name='empty')[0]
        except IndexError:
            album = Album(name='empty', artist = Aritst.get_default())
            album.save()
            album.genres.add(Genre.get_default())
            album.save()
        return album

class Song(models.Model):
    name=models.CharField(max_length=200)
    artist=models.ForeignKey('Artist')
    genres=models.ManyToManyField('Genre')
    album=models.ForeignKey('Album')
    link=models.CharField(max_length=2000)
    def __unicode__(self):
        return self.name


    @staticmethod
    def get_default():
        try:
            song = Song.objects.filter(name='empty')[0]
        except IndexError:
            song = Song(name='empty', artist = Artist.get_default(),
                        album = Album.get_default(), link="youtube.com")
            song.save()
            song.genres.add(Genre.get_default())
            song.save()
        return song

class Guy(models.Model):
    user=models.OneToOneField(User)
    favsongs=models.ManyToManyField('Song')
    favartists=models.ManyToManyField('Artist')
    favgenres=models.ManyToManyField('Genre')
    def __unicode__(self):
        return self.user.username

    @staticmethod
    def make_default(user):
        guy = Guy(user=user)
        guy.save()
        guy.favsongs.add(Song.get_default())
        guy.favartists.add(Artist.get_default())
        guy.favgenres.add(Genre.get_default())
        guy.save()
        return guy

class post(models.Model):
	text=CharField(max_length=10000)
	poster=
