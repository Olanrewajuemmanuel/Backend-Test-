from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)
    name = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "name")
