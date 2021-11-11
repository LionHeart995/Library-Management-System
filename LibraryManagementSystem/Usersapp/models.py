from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class User(AbstractBaseUser):
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(max_length=100, default='', unique=True)
	password1 = models.CharField(max_length=16, default='0',validators=[alphanumeric])
	password2 = models.CharField(max_length=16, default='0',validators=[alphanumeric])

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	class Meta:
		db_table = 'user'

	def __str__(self):
		return str(self.email)
