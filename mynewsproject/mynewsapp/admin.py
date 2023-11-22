from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AllNews

#admin.site.register(AllNews)

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

class AllNewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'link', 'time', 'has_image', 'is_active']
    actions = [set_active]


admin.site.register(AllNews, AllNewsAdmin)

