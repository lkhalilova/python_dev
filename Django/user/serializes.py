from rest_framework import serializers

from purchase.serializes import PurchaseSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

