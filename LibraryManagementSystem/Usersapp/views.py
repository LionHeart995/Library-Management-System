from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm


def login(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			fm = AuthenticationForm(request=request, data=request.POST)
			if fm.is_valid():
				email = fm.cleaned_data['email']
				password = fm.cleaned_data['password']
				user = auth.authenticate(email=email, password=password)
				if user is not None:
					auth.login(request, user)
					messages.info(request, 'Invalid Credentials')
					return render(request, 'books/displayBooks.html')
			else:
				fm = AuthenticationForm()
				return render(request, 'user/login.html', {'form': fm})
	else:
		return render(request, 'books/displayBooks.html')


def signup(request):
	fm = SignUpForm
	if request.method == 'POST':
		fm = SignUpForm(request.POST)
		if fm.is_valid():
			fm.save()
			messages.success(request, 'Successfully Created Account')
			return render(request, 'user/login.html')
		else:
			fm = SignUpForm()
	else:
		fm = SignUpForm()
	return render(request, 'user/signup.html', {'form': fm})


def logout(request):
	auth.logout(request)
	return render(request, 'user/logout.html')
