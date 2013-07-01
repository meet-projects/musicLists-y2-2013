# Create your views here.
from django.shortcuts import render

def showSignUp(request):
	context = {}
    	return render(request, 'music/signup.html', context)
