# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def showSignUp(request):
	context = {}
    	return render(request, 'music/signup.html', context)
def submitlogin(request):
        UserName=request.POST['username']
	Password=request.POST['password']
	return HttpResponseRedirect('music/profile.HTML')
def signup(request):
	Email=request.POST["user[email]"]
	Password=request.POST["user[password]"]
	UserName=request.POST["tumblelog[name]"]
	FirstName=request.POST["firstname"]
	LastName=request.POST["lastname"]
	newser = User.objects.create_user(username=UserName, email=Email, password=Password, first_name=FirstName, last_name=LastName)
	return HttpResponse("working, account created")


	
