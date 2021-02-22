#This is my views.py file :D

from django.shortcuts import render

# Create home HTML here. When you want to enter webpage, you send a "request".
def home(request):
	#This is our view.
	return render(request, 'home.html', {})

def about(request):
	#This is our view.
	return render(request, 'about.html', {})	