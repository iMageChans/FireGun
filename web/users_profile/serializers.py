from rest_framework import serializers
from .models import UserBurningProfile


class UserBurningProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBurningProfile
        fields = '__all__'