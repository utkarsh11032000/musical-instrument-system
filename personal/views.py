from django.shortcuts import render

from account.models import Account


def home_screen_view(request):
	
	context = {}

	accounts = Account.objects.all()
	context['accounts'] = accounts

	return render(request, "personal/home.html", context)

def piano_view(request):

	return render(request, "personal/piano.html")

def test_piano_view(request):

	return render(request, "personal/test_piano.html")

def quiz_view(request):

	return render(request, "personal/quiz.html")

def guitar_view(request):

	return render(request, "personal/guitar.html")