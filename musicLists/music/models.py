from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Guy(models.Model):
    user=models.ForeignKey('User')
    favsongs=models.ManyToManyField('song')
    favartists=models.ManyToManyField('artist')
    favgenres=models.ManyToManyField('genre')
    def __unicode__(self):
        return self.user.username

class Song(models.Model):
    name=models.CharField(max_length=200)
    artist=models.ForeignKey('Artist')
    genres=models.ManyToManyField('genre')
    album=models.ForeignKey('album')
    link=models.CharField(max_length=2000)
    def __unicode__(self):
        return self.name

class Artist(models.Model):
    name=CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Album(models.Model):
    artist=models.ForeignKey('artist')
    genres=models.ManyToManyField('genre')
    
    
class Genre(models.Model):
    name=models.CharField(max_length=200)
    
`
