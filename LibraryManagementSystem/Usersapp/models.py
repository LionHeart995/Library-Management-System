from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password, first_name, last_name, **extra_fields):
		if not email:
			raise ValueError('The Email must be set')
		if not password:
			raise ValueError('password is not provided')

		email = self.normalize_email(email)
		user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, email, password, first_name, last_name, **extra_fields):

		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(email, password, first_name, last_name, **extra_fields)

	def create_superuser(self, email, password, first_name, last_name, **extra_fields):

		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(email, password, first_name, last_name, **extra_fields)


class User(AbstractUser):
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(db_index=True, max_length=100, unique=True)
	# password1 = models.CharField(max_length=16, default='0', validators=[alphanumeric])
	# password2 = models.CharField(max_length=16, default='0', validators=[alphanumeric])

	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = CustomUserManager()

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'

	def __str__(self):
		return self.email
