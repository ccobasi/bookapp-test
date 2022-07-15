from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "second_name",
        )


class BookSerializer(serializers.ModelSerializer):
    Authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "isbn",
            "author",
        )
