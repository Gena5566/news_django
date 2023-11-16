from django.test import TestCase
from django.utils import timezone
from faker import Faker  # Импортируем класс Faker
from usersapp.models import BlogUser
from .models import AllNews

class AllNewsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        faker = Faker()  # Создаем экземпляр Faker
        # Создаем пользователя BlogUser, используя Faker
        user = BlogUser.objects.create(username=faker.name())
        print(f"Generated username: {user.username}")  # Выводим сгенерированное имя

        # Создаем экземпляр AllNews, используя Faker и созданного пользователя
        AllNews.objects.create(
            title='Test News',
            link='http://example.com',
            time=timezone.now(),
            image_url='http://example.com/image.jpg',
            content='This is a test news content.',
            user=user  # Используем созданный экземпляр пользователя
        )

    def test_has_image(self):
        news = AllNews.objects.get(id=1)
        self.assertTrue(news.has_image())

    def test_some_method(self):
        news = AllNews.objects.get(id=1)
        self.assertEqual(news.some_method(), 'hello from method')

    def test_str_method(self):
        news = AllNews.objects.get(id=1)
        self.assertEqual(str(news), 'Test News')



