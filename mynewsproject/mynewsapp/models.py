from django.db import models
from datetime import datetime


class AllNews(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)  # Установите значение по умолчанию как строку
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='index', null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title






