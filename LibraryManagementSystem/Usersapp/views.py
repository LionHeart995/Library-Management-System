from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .forms import SignUpForm


def login(request):
	return render(request, 'user/login.html')


def signup(request):
	SignUp = SignUpForm
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1==password2:
			if User.objects.filter(email=email).exists():
				messages.info(request,'Username Taken')
			else:
				user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password1)
				user.save()
				messages.info(request, 'User Created')
		else:
			messages.info(request, 'User Created')
		return redirect('/')
	else:
		return render(request, 'user/signup.html', {'SignUpForm': SignUp})


def logout(request):
	return render(request, 'user/logout.html')
