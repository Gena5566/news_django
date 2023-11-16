from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AllNews

#admin.site.register(AllNews)


class AllNewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'link', 'time', 'has_image']


admin.site.register(AllNews, AllNewsAdmin)

