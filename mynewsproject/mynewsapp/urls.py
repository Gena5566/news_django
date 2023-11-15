from django.urls import path

from .views import IndexView, AllNewsView, ContactView, create_post_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Главная страница
    path('all_news/<int:id>/', AllNewsView.as_view(), name='all_news'),  # Страница с новостями
    path('contact/', ContactView.as_view(), name='contact'),
    #path('create/', CreatePostView.as_view(), name='create'),
    path('create/', create_post_view, name='create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



