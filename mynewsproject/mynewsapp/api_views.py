from .models import AllNews
from .serializers import AllNewsSerializer, PostSerializer
from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .permissions import ReadOnly, IsAuthor



class AllNewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = AllNews.objects.all()
    serializer_class = AllNewsSerializer

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthor | ReadOnly]
    queryset = AllNews.objects.all()
    serializer_class = PostSerializer

class ContactMessageListCreateView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
