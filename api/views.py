from django.shortcuts import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from api import serializers


class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class AuthorList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAuthor(request, pk):
    authors = Author.objects.get(id=pk)
    serializer = AuthorSerializer(authors, many=False)
    return Response(serializer.data)

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
