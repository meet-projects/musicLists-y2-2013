# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def showSignUp(request):
	context = {}
    	return render(request, 'music/signup.html', context)
def profile(request):
	context = {}
    	return render(request, 'music/profile.html', context)
def submitlogin(request):
        UserName=request.POST['username']
	Password=request.POST['password']
<<<<<<< HEAD
	return HttpResponseRedirect('music/profile.HTML')
=======
	user=authenticate(username=UserName, password=Password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect('profile')
	return HttpResponseRedirect('signup')
>>>>>>> f42defa0ce04273862557bf8723f1e214cd8f496
def signup(request):
	Email=request.POST["user[email]"]
	Password=request.POST["user[password]"]
	UserName=request.POST["tumblelog[name]"]
	FirstName=request.POST["firstname"]
	LastName=request.POST["lastname"]
	newser = User.objects.create_user(username=UserName, email=Email, password=Password, first_name=FirstName, last_name=LastName) 
	return render('profile')
