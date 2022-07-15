from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


# class BookDetail(APIView):
#     def get_object(self, author, name):
#         try:
#             return Book.objects.filter(category__slug=category_slug).get(slug=Book_slug)
#         except Book.DoesNotExist:
#             raise Http404

#     def get(self, request, category_slug, Book_slug, format=None):
#         Book = self.get_object(category_slug, Book_slug)
#         serializer = BookSerializer(Book)
#         return Response(serializer.data)

# class CategoryDetail(APIView):
#     def get_object(self, category_slug):
#         try:
#             return Category.objects.get(slug=category_slug)
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self, request, category_slug, format=None):
#         category = self.get_object(category_slug)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

# @api_view(['POST'])
# def search(request):
#     query = request.data.get('query', '')

#     if query:
#         Books = Book.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
#         serializer = BookSerializer(Books, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({"Books": []})
