from .models import AllNews
from .serializers import AllNewsSerializer, PostSerializer
from rest_framework import viewsets



class AllNewsViewSet(viewsets.ModelViewSet):
    queryset = AllNews.objects.all()
    serializer_class = AllNewsSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = AllNews.objects.all()
    serializer_class = PostSerializer

