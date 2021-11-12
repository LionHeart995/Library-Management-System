from django.urls import path
from . import views

urlpatterns = [
	path('', views.displayBook, name='displayBook'),
	path('addBook', views.addBook, name='addBook'),
	path('deleteBook', views.deleteBook, name='deleteBook'),
	path('displayBook', views.displayBook, name='displayBook'),
	path('updateBook', views.updateBook, name='updateBook'),

]
