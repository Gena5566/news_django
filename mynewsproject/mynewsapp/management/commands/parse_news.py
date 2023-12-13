from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By  # Добавьте эту строку
from mynewsapp.models import AllNews
import schedule
import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime


class Command(BaseCommand):
    help = 'Parse news and save to the database'

    def handle(self, *args, **options):
        # Получаем текущего пользователя
        from usersapp.models import BlogUser  # Замените 'usersapp' на путь к вашему приложению
        user = BlogUser.objects.get(username='Gena')

        # Настройка расписания выполнения парсинга каждые 1 минуту
        schedule.every(1).minutes.do(lambda: self.parse_and_save_news(user))

        while True:
            schedule.run_pending()
            time.sleep(1)
            self.stdout.write("Waiting for the next scheduled execution...")

    # Обновленный метод parse_and_save_news с добавлением параметра user
    def parse_and_save_news(self, user):
        with webdriver.Chrome() as driver:
            url = 'https://habr.com/ru/flows/develop/articles/'
            driver.get(url)

            image_elements = driver.find_elements(By.CSS_SELECTOR, '.tm-article-snippet__cover img')
            image_urls = []

            for image_element in image_elements:
                image_url = image_element.get_attribute('src')
                image_urls.append(image_url)

            title_elements = driver.find_elements(By.CSS_SELECTOR, '.tm-title.tm-title_h2 a')
            time_elements = driver.find_elements(By.CSS_SELECTOR, '.tm-article-snippet time')

            for i in range(len(title_elements)):
                title = title_elements[i].text.strip()
                link = title_elements[i].get_attribute('href')
                time_str = time_elements[i].get_attribute('title')
                image_url = image_urls[i] if i < len(image_urls) else None  # None, если изображение не найдено

                # Попробуем преобразовать строку времени в объект datetime
                try:
                    publication_time = datetime.strptime(time_str, "%Y-%m-%d, %H:%M")
                except ValueError:
                    self.stdout.write(f"Skipped news: {title} (incorrect time)")
                    continue

                # Проверка, сохранена ли новость с такой ссылкой и временем публикации
                if not AllNews.objects.filter(link=link, time=publication_time, user=user).exists():
                    self.stdout.write(f"Title: {title}")
                    self.stdout.write(f"Link: {link}")
                    self.stdout.write(f"Publication Time: {publication_time}")
                    if image_url is not None:
                        self.stdout.write(f"Image URL: {image_url}")

                        # Создаем и сохраняем объект
                        news_article = AllNews(
                            title=title,
                            link=link,
                            time=publication_time,
                            image_url=image_url,
                            user=user,  # Добавлено значение user
                        )
                        news_article.save()
                        self.stdout.write("Data saved to the database")
                    else:
                        self.stdout.write("Skipped news: image not found")
                else:
                    self.stdout.write(f"Skipped news: {title} (already saved in the database)")