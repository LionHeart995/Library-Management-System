from django.shortcuts import render


# Create your views here.
def addBook(request):
	return render(request, 'books/addBook.html')


def deleteBook(request):
	return render(request, 'books/deleteBook.html')


def displayBook(request):
	return render(request, 'books/displayBooks.html')


def updateBook(request):
	return render(request, 'books/updateBook.html')
