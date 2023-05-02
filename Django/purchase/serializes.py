from rest_framework import serializers
from .models import Purchase
from user.serializes import UserSerializer
from book.serializes import BookSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(method_name="id_method")
    users = UserSerializer(many=True)
    book = BookSerializer(many=True)

    def id_method(self, obj):
        return f"Purchase's id: {obj.id}"

    class Meta:
        model = Purchase
        fields = "__all__"

