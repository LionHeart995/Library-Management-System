from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
	SignUp = SignUpForm
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'Username Taken')
			else:
				form = SignUpForm(request.POST or None)
				if form.is_valid():
					form.save()
					print(form)

					user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password1)
					user.save()
					messages.info(request, 'User Created')
					return redirect('login')
				context = {'form': form}
				return render(request, 'user/signup.html', context)
		else:
			messages.info(request, 'Password does not match')
		return redirect('/')
	else:
		return render(request, 'user/signup.html', {'SignUpForm': SignUp})


def logout(request):
	auth.logout(request)
	return render(request, 'user/logout.html')
