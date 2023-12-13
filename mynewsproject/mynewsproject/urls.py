from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mynewsapp.urls')),  # Включаем URL-пути из вашего приложения
    path('users/', include('usersapp.urls', namespace='users')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    # Обслуживание медиа-файлов в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






