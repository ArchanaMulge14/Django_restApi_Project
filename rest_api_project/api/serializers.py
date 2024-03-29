# app_name/serializers.py

from rest_framework import serializers
from .models import CustomUser, Paragraph

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'dob', 'created_at', 'modified_at']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'user', 'created_at']
