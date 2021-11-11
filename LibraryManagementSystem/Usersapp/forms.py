from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

x1 = forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'})
x2 = forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Confirm Password'})
x3 = forms.TextInput(attrs={'class': "form-control", 'placeholder': 'First Name'})
x4 = forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last Name'})
x6 = forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'})
x7 = forms.TextInput(attrs={'class': "form-control"})


# Sign Up Forms

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, widget=x3, label=False)
	last_name = forms.CharField(max_length=30, required=True, widget=x4, label=False)
	email = forms.EmailField(max_length=254, required=True, widget=x6, label=False)
	password1 = forms.CharField(required=True, widget=x1, label=False)
	password2 = forms.CharField(required=True, widget=x2, label=False)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
