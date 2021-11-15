from django.urls import path
from . import views

urlpatterns = [
	# path('', views.displayBook, name='displayBook'),
	path('addBook', views.addBook, name='addBook'),
	path('deleteBook/<int:id>/', views.deleteBook, name='deleteBook'),
	path('displayBook', views.displayBook, name='displayBook'),
	path('updateBook', views.updateBook, name='updateBook'),
	path('base', views.base, name='base'),

]
