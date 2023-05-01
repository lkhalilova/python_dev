import datetime

from django.db import models
from user.models import User
from book.models import Book
from django.forms import ModelForm, DateField, DateInput


class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, related_name="purchases", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="purchases", on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)

    def __str__(self):
        return f"{self.id}: {self.user.first_name} {self.user.last_name} {self.book.title} {self.date} "

    class Meta:
        ordering = ["-date"]


class PurchaseForm(ModelForm):

    class Meta:
        model = Purchase
        fields = ("id", "user", "book", "date")



