from django.db import models
from django.forms import ModelForm


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} {self.age}"


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "age")

