from django.db import models

from library.models.author import Author
from library.models.publisher import Publisher


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title