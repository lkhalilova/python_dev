from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(method_name="id_method")

    def id_method(self, obj):
        return f"User's id: {obj.id}"

    class Meta:
        model = User
        fields = "__all__"

