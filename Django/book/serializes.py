from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(method_name="id_method")

    def id_method(self, obj):
        return f"Book's id: {obj.id}"

    class Meta:
        model = Book
        fields = "__all__"

