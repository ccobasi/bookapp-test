from tkinter import CASCADE
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
        Author, related_name="authors", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
