from django import forms
from .models import BookDetails

x1 = forms.TextInput(attrs={'class': "form-control"})
x2 = forms.NumberInput(attrs={'class': "form-control"})
x3 = forms.FileInput(attrs={'class': "form-control"})
x4 = forms.DateField(attrs={'class': "form-control"})


class addBookDetails(forms.ModelForm):
	BookID = forms.IntegerField(required=True, widget=x2)
	BookTitle = forms.CharField(required=True, widget=x1)
	BookAuthor = forms.CharField(required=True, widget=x1)
	BookEdition = forms.CharField(required=True, widget=x1)
	BookPrice = forms.IntegerField(required=True, widget=x2)
	BookLanguage = forms.CharField(required=True, widget=x1)
	BookCategory = forms.CharField(required=True, widget=x1)
	BookPublicationYear = forms.CharField(required=True, widget=x4)

	class Meta:
		model = BookDetails
		fields = ['BookID', 'BookTitle', 'BookAuthor', 'BookEdition', 'BookPrice', 'BookLanguage', 'BookCategory','BookPublicationYear']


class updateBookDetails(forms.ModelForm):
	BookID = forms.IntegerField(required=True, widget=x2)
	BookTitle = forms.CharField(required=True, widget=x1)
	BookAuthor = forms.CharField(required=True, widget=x1)
	BookEdition = forms.CharField(required=True, widget=x1)
	BookPrice = forms.IntegerField(required=True, widget=x2)
	BookLanguage = forms.CharField(required=True, widget=x1)
	BookCategory = forms.CharField(required=True, widget=x1)
	BookPublicationYear = forms.CharField(required=True, widget=x4)

	class Meta:
		model = BookDetails
		fields = ['BookID', 'BookTitle', 'BookAuthor', 'BookEdition', 'BookPrice', 'BookLanguage', 'BookCategory','BookPublicationYear']
