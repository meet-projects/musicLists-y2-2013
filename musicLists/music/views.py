# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from models import Artist, Song, Guy, Genre, Album

 
def showSignUp(request):
	context = {}
    	return render(request, 'music/signup.html', context)

@login_required
def homepage(request):
	context = {}
    	return render(request, 'music/homepage.html', context)

@login_required
def profile(request):
	context = {'user': request.user}
    	return render(request, 'music/profile.html', context)

def submitlogin(request):
        UserName=request.POST['username']
	Password=request.POST['password']
	user=authenticate(username=UserName, password=Password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect('/homepage')
        request.user.guy
	return HttpResponseRedirect('/signUp')

def signup(request):
	Email=request.POST["email"]
	Password=request.POST["password"]
	UserName=request.POST["name"]
	FirstName=request.POST["firstname"]
	LastName=request.POST["lastname"]
	newser = User.objects.create_user(username=UserName, email=Email, password=Password, first_name=FirstName, last_name=LastName)
	guy = Guy.make_default(newser)
	return HttpResponseRedirect('/profile')

def logout(request):
	logout(request)
	#redirect

