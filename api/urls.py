from django.urls import path, include

from . import views

urlpatterns = [
    path('book-lists/', views.BookList.as_view()),
]
