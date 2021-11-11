from django.urls import path
from . import views

urlpatterns = [
	path('', views.displayBook, name='displayBook'),
	path('addBook', views.addBook, name='login'),
	path('deleteBook', views.deleteBook, name='logout'),
	path('displayBook', views.displayBook, name='displayBook'),
	path('updateBook', views.updateBook, name='updateBook'),

]
