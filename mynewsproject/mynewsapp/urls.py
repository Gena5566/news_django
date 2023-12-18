from django.urls import path, include
from .views import IndexView, AllNewsView, ContactView, create_post_view, SimpleMainAjax
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from .api_views import AllNewsViewSet, PostViewSet, ContactMessageListCreateView
from mynewsapp import views

#router = DefaultRouter()
#router.register(r'allnews', AllNewsViewSet, basename='allnews')

#router = DefaultRouter()
#router.register(r'posts', PostViewSet, basename='posts')

router = DefaultRouter()
router.register(r'allnews', AllNewsViewSet, basename='allnews')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'contact', ContactMessageListCreateView, basename='contact')


urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Главная страница
    path('all_news/<int:id>/', AllNewsView.as_view(), name='all_news'),  # Страница с новостями
    path('users/', include('usersapp.urls', namespace='users')),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/', create_post_view, name='create'),
    path('api/v0/', include(router.urls)),
    path('simple/', views.SimpleMainAjax.as_view(), name='simple_ajax'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



