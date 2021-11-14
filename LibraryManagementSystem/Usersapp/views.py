from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .forms import SignUpForm


def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(email=email, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")

	else:
		messages.info(request, 'Invalid Credentials')
		return render(request, 'user/login.html')


def signup(request):
	if request.method == 'POST':
		fm = SignUpForm(request.POST)
		if fm.is_valid():
			fm.save()
			messages.success(request, 'Successfully Created Account')
	else:
		fm = SignUpForm()
	return render(request, 'user/signup.html', {'form': fm})


def logout(request):
	auth.logout(request)
	return render(request, 'user/logout.html')
