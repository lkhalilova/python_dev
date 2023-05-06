from django.db import models
from user.models import User


class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)
    readers = models.ManyToManyField(User, related_name="books")

    class Meta:
        unique_together = ("title", "author")

