from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class User(AbstractUser):
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(max_length=100, default='', unique=True)
	password1 = models.CharField(max_length=16, default='0',validators=[alphanumeric])
	password2 = models.CharField(max_length=16, default='0',validators=[alphanumeric])

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return str(self.email)
