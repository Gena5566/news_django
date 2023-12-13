from django.urls import path, include
from .models import AllNews
from rest_framework import routers, serializers, viewsets

class AllNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllNews
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllNews
        fields = '__all__'








