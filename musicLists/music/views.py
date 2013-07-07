# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from models import Artist, Song, Guy, Genre, Album, Postclass

 
def showSignUp(request):
	context = {}
    	return render(request, 'music/signup.html', context)

@login_required
def homepage(request):
	context = {}
    	return render(request, 'music/homepage.html', context)

@login_required
def profile(request):
        user = request.user
	context = {}
    	return render(request, 'music/profile.html', context)

def submitlogin(request):
        UserName=request.POST['username']
	Password=request.POST['password']
	user=authenticate(username=UserName, password=Password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect('/homepage')
	return HttpResponseRedirect('/signUp')

def signup(request):
	Email=request.POST["email"]
	Password=request.POST["password"]
	UserName=request.POST["name"]
	FirstName=request.POST["firstname"]
	LastName=request.POST["lastname"]
	newser = User.objects.create_user(username=UserName, email=Email, password=Password, first_name=FirstName, last_name=LastName)
	Guy(user=newser).save()
	user = authenticate(username=UserName, password=Password)
	login(request, user)
	return HttpResponseRedirect('/profile')

@login_required
def addsong(request):
	songname = request.POST['songname']
	if not len(songname):
		return HttpResponseRedirect('/addsong')
	artist_name=request.POST['artist']
	album_name=request.POST['album']
	genre=request.POST['genre']
	link=request.POST['link']
	genre = Genre.objects.filter(name=genre)[0]
	if len(artist_name):
		artist = Artist.objects.filter(name=artist_name)
		if not len(artist):
			artist=Artist(name=artist_name)
			artist.save()
		else:
			artist = artist[0]
	else:
		artist = Artist.get_default()
	if len(album_name):
		album = Album.objects.filter(name=album_name)
		if not len(album):
			album=Album(name=album_name, artist=artist)
			album.save()
			album.genres.add(genre)
			album.save()
		else:
			album = album[0]
	else:
		album = Album.get_default()
	song = Song.objects.filter(name=songname)
	if not len(song):
		song=Song(name=songname, artist=artist, album=album, link=link)
		song.save()
		song.genres.add(genre)
		song.save()
	else:
		song = song[0]
	guy = Guy.objects.filter(user=request.user)[0]
	guy.favsongs.add(song)
	guy.save()
        return HttpResponseRedirect('/profile')

@login_required
def showaddsongs(request):
	genres = Genre.objects.all()
	return render(request,'music/addsongs.html',{'genres': genres})

@login_required
def showaddartist(request):
	return render(request,'music/addartist.html')


def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/signUp')

@login_required
def add_post(request):
	text=request.POST['xhpc_message_text']
	new_post=Postclass(texti=text, poster=request.user.guy)
	new_post.save()
	return HttpResponseRedirect('/profile')

def addartist(request):
	artist_name=request.POST['artist']
	if not len(artist_name):
		return HttpResponseRedirect('/addsong')
	artist = Artist.objects.filter(name=artist_name)
	if not len(artist):
		artist=Artist(name=artist_name)
		artist.save()
	else:
		artist = artist[0]
	guy = Guy.objects.filter(user=request.user)[0]
	guy.favartists.add(artist)
	guy.save()
        return HttpResponseRedirect('/profile')

def addalbum(request):
	album_name=request.POST['album']
	if not len(album_name):
		return HttpResponseRedirect('/addalbum')
	genre=request.POST['genre']
	artist_name=request.POST['artist']
	genre = Genre.objects.filter(name=genre)[0]

	if len(artist_name):
		artist = Artist.objects.filter(name=artist_name)
		if not len(artist):
			artist=Artist(name=artist_name)
			artist.save()
		else:
			artist = artist[0]
	else:
		artist = Artist.get_default()
	album= Album.objects.filter(name=album_name)
	if not len(album):
		print genre
		album=Album(name=album_name, artist=artist)
		album.save()
		album.genres.add()
		album.save()
		
	else:
		album = album[0]
	guy = Guy.objects.filter(user=request.user)[0]
	guy.favalbums.add(album)
	guy.save()
        return HttpResponseRedirect('/profile')

def showaddalbum(request):
	genres = Genre.objects.all()
	return render(request,'music/addalbum.html',{'genres': genres})


	

