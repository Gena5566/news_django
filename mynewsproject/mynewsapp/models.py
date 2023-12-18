# mynewsproject/mynewsapp/models.py
from django.db import models
from usersapp.models import BlogUser

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

    class Meta:
        abstract = True

class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='index', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class AllNews(BaseModel):
    objects = models.Manager()
    active_objects = ActiveManager()

    def has_image(self):
        return self.image is not None

    def some_method(self):
        return 'hello from method'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name







