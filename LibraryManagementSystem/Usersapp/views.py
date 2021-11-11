from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm


def login(request):
	return render(request, 'user/login.html')


def signup(request):
	SignUp = SignUpForm
	return render(request, 'user/signup.html', {'SignUpForm': SignUp})


def logout(request):
	return render(request, 'user/logout.html')
