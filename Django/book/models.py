from django.db import models
from django.forms import ModelForm


class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.id}: {self.title} {self.author} {self.year} {self.price} hrivnas"

    class Meta:
        unique_together = ("title", "author")


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "year", "price")

