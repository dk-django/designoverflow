from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DalleGeneration


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DalleGeneration
        fields = ['id', 'owner', 'user_prompt', 'dalle_response', 'created_at']
    # id = serializers.IntegerField()
    # user_prompt = serializers.CharField(max_length=4000)
    # dalle_response = serializers.CharField(max_length=4000)
    owner = serializers.StringRelatedField(read_only=True)

    