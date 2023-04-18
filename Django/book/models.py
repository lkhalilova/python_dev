from django.db import models


class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)

    class Meta:
        unique_together = ("title", "author")

