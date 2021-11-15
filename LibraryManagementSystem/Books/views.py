from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import addBookDetails, updateBookDetails
from .models import BookDetails
from .serializers import BookDetailsSerializer


# Create your views here.

class BookDetailsList(APIView):
	def get(self, request):
		bkDetails = BookDetails.objects.all()
		serializer = BookDetailsSerializer(bkDetails, many=True)
		return Response(serializer.data)

	def post(self, request):
		pass


def base(request):
	return render(request, 'books/base.html', {'name': request.first_name})


def addBook(request):
	if request.method == 'POST':
		bk = addBookDetails(request.POST)
		if bk.is_valid():
			x1 = bk.cleaned_data['BookID']
			x2 = bk.cleaned_data['BookTitle']
			x3 = bk.cleaned_data['BookAuthor']
			x4 = bk.cleaned_data['BookEdition']
			x5 = bk.cleaned_data['BookPrice']
			x6 = bk.cleaned_data['BookLanguage']
			x7 = bk.cleaned_data['BookCategory']
			x8 = bk.cleaned_data['BookPublicationYear']
			reg = BookDetails(BookID=x1, BookTitle=x2, BookAuthor=x3, BookEdition=x4, BookPrice=x5, BookLanguage=x6,
			                  BookCategory=x7, BookPublicationYear=x8)
			reg.save()
		else:
			bk = addBookDetails()
	return render(request, 'books/addBook.html', {'BookDetails': bk})


def deleteBook(request):
	bkDetails = BookDetails.objects.filter()
	if request.method == 'POST':
		pi = BookDetails.object.get(pk=id)
		pi.delete()
	return render(request, 'books/deleteBook.html', {'bookDetails': bkDetails})


def displayBook(request):
	bkDetails = BookDetails.objects.all()
	return render(request, 'books/displayBooks.html', {'bookDetails': bkDetails})


def updateBook(request, id):
	bkDetails = BookDetails.objects.all()
	if request.method == 'POST':

		bk = updateBookDetails(request.POST)

		if bk.is_valid():
			x1 = bk.cleaned_data['BookID']
			x2 = bk.cleaned_data['BookTitle']
			x3 = bk.cleaned_data['BookAuthor']
			x4 = bk.cleaned_data['BookEdition']
			x5 = bk.cleaned_data['BookPrice']
			x6 = bk.cleaned_data['BookLanguage']
			x7 = bk.cleaned_data['BookCategory']
			x8 = bk.cleaned_data['BookPublicationYear']
			reg = BookDetails(BookID=x1, BookTitle=x2, BookAuthor=x3, BookEdition=x4, BookPrice=x5, BookLanguage=x6,
			                  BookCategory=x7, BookPublicationYear=x8)
			reg.save()
		else:
			bk = addBookDetails()
	return render(request, 'books/updateBook.html', {'bookDetails': bk})
