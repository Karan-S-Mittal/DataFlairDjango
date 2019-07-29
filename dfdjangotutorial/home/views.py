from django.shortcuts import render
#DataFlair
#Karan Mittal

def index(request):
	return render(request, 'home/base.html')

def other(request):
	context = {
	'k1': 'Welcome to the Second page',
	}
	return render(request, 'home/other.html', context)

