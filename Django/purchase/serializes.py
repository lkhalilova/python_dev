from rest_framework import serializers
from .models import Purchase
from user.serializes import UserSerializer
from book.serializes import BookSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()

    class Meta:
        model = Purchase
        fields = ("id", "date", "user", "book")


