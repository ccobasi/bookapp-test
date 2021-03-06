# from tkinter import CASCADE
from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.first_name


class Book(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.book.id}/'
