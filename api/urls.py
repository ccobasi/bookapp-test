from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('book-lists/', views.BookList.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('books/<str:pk>/update', views.updateBook, name="update-book"),
    path('books/<str:pk>/', views.getBook, name="book"),
    path('authors/<str:pk>/update', views.updateAuthor, name="update-author"),
    path('authors/<str:pk>/', views.getAuthor, name="author"),

]
