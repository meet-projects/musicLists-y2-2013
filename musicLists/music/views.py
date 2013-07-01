# Create your views here.
from django.shortcuts import render

def showSignUp(request):
	context = {}
    	return render(request, 'music/signup.html', context)
def submitlogin(request):
        UserName=request.POST['username']
	Password=request.POST['password']
	return HttpResponseRedirect('profile')
def signup(request):
	Email=request.POST["user[email]"]
	Password=request.POST["user[password]"]
	UserName=request.POST["tumblelog[name]"]
	FirstName=request.POST["firstname"]
	LastName=request.POST["lastname"]
	newser=Guy(
	
