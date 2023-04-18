from django.db import models
from user.models import User
from book.models import Book


class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, related_name="purchases", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="purchases", on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        ordering = ["-date"]


