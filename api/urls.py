from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('book-lists/', views.BookList.as_view()),
    path('detail/<int:book_id>/', BookDetail.as_view()),
]
