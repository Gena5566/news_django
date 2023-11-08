from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mynewsapp.urls')),  # Включаем URL-пути из вашего приложения
]





