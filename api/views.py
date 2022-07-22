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


@api_view(['POST'])
def createAuthor(request):
    data = request.data
    author = Author.objects.create(
        body=data['body']
    )
    serializer = AuthorSerializer(instance=author, many=False)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def createBook(request):
    data = request.data
    book = Book.objects.create(
        body=data['body']
    )
    serializer = BookSerializer(instance=book, many=False)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateAuthor(request, pk):
    data = request.data
    author = Author.objects.get(id=pk)
    serializer = AuthorSerializer(instance=author, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateBook(request, pk):
    data = request.data
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
