from django.db import models


# Create your models here.
class BookDetails(models.Model):
	BookID = models.IntegerField(default=0, primary_key=True)
	BookTitle = models.CharField(max_length=100, default='')
	BookAuthor = models.CharField(max_length=100, default='')
	BookEdition = models.CharField(max_length=100, default='')
	BookPrice = models.CharField(max_length=10, default='')
	BookLanguage = models.CharField(max_length=50, default='')
	BookCategory = models.CharField(max_length=50, default='')
	BookPublicationYear = models.CharField(max_length=5, default='')

	def __str__(self):
		return str(self.BookID)
