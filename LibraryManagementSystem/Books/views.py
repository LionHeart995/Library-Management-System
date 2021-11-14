from django.shortcuts import render
from .models import BookDetails
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
	return render(request, 'books/addBook.html')


def deleteBook(request):
	return render(request, 'books/deleteBook.html')


def displayBook(request):
	bkDetails = BookDetails.objects.all()
	return render(request, 'books/displayBooks.html', {'bookDetails': bkDetails})


def updateBook(request):
	return render(request, 'books/updateBook.html')
