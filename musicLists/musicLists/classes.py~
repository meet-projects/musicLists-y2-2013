from django.db import models

class user(models.Model):
    firstname=CharField(max_length=20)
    lastname=CharField(max_length=20)
    nickname=CharField(max_length=15)
    password=CharField(min_length=6, max_length=20)
    birthday=models.DateField(blank=True, null=True)
    favgenres=ForeignKey('genre')
    favalbums=ForeingKey('album)
    friends=ForeignKey('user')
    favsongs=ForeignKey('song')
    favartists=ForeignKey('artist')

class song(models.Model):
    songname=CharField(max_length=1000)
    artist=ForeignKey('artist')
    genre=



