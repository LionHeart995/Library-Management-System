from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class User(models.Model):
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(max_length=100, default='', unique=True)
	password1 = models.CharField(max_length=16, default='0',validators=[alphanumeric])
	password2 = models.CharField(max_length=16, default='0',validators=[alphanumeric])

	def __str__(self):
		return str(self.email)
