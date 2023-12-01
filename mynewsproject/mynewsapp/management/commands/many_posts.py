from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from mynewsapp.models import AllNews  # Исправленный импорт
from usersapp.models import BlogUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        AllNews.objects.all().delete()
        BlogUser.objects.filter(is_superuser=False).delete()  # Убедитесь, что is_superuser не будет установлено в True для созданных пользователей

        count = 500
        for i in range(count):
            p = (i/count)*100
            print(f'{i}) {p} %')
            mixer.blend(AllNews)  #  вызов для создания постов

        print('end')
