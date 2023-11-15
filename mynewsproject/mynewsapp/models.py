from django.db import models
from usersapp.models import BlogUser

class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='index', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class AllNews(BaseModel):
    # Дополнительные поля,  для модели AllNews
    pass
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'






