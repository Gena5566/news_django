from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from mynewsapp.models import AllNews
import datetime
import schedule
import time
from datetime import timedelta

class Command(BaseCommand):
    help = 'Parse news and save to the database'

    def handle(self, *args, **options):
        # Настройка расписания выполнения парсинга каждые 1 минута
        schedule.every(1).minutes.do(self.parse_and_save_news)

        while True:
            schedule.run_pending()
            time.sleep(1)
            print("Waiting for the next scheduled execution...")

    def parse_and_save_news(self):
        url = 'https://ria.ru/world/'
        response = requests.get(url)

        if response.status_code == 200:
            print("Parsing news...")
            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.find_all(class_='list-item')

            for item in news_items:
                title = item.find(class_='list-item__title').text.strip()
                link = item.find(class_='list-item__title')['href']

                # Проверка, сохранена ли новость с такой ссылкой
                if not AllNews.objects.filter(link=link).exists():
                    date_tag = item.find(class_='list-item__date')
                    publication_time = self.parse_date(date_tag.text.strip())

                    image_tag = item.find(class_='responsive_img')
                    image_url = image_tag['src'] if image_tag else None

                    if publication_time:
                        print(f"Publication time for {title}: {publication_time}")
                        news_article = AllNews(
                            title=title,
                            link=link,
                            time=publication_time,
                            image_url=image_url
                        )
                        news_article.save()  # Сохраняем новость в базу данных
                        print(f"Saved news: {title}")

    def parse_date(self, date_string):
        try:
            publication_time = datetime.datetime.strptime(date_string, '%H:%M')
            current_date = datetime.date.today()
            publication_time = datetime.datetime.combine(current_date, publication_time.time())  # Присоединяем текущую дату к времени
            return publication_time
        except ValueError:
            print(f"Ошибка при парсинге времени: {date_string}")
            return None









