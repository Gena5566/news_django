from django.urls import path, include
from .models import AllNews, ContactMessage
from rest_framework import routers, serializers, viewsets

class AllNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllNews
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllNews
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message']






