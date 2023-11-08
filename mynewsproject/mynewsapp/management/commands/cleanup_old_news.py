from django.core.management.base import BaseCommand
from mynewsapp.models import AllNews
import datetime
import schedule
import time

class Command(BaseCommand):
    help = 'Cleanup the database by removing old news'

    def handle(self, *args, **options):
        # Расписание выполнения очистки базы данных
        schedule.every(24).hours.do(self.cleanup_database)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def cleanup_database(self):
        older_than = datetime.datetime.now() - datetime.timedelta(days=1)
        AllNews.objects.filter(time__lt=older_than).delete()
        self.stdout.write(self.style.SUCCESS('Database cleanup complete.'))


        # Записать результат в лог
        with open('cleanup_log.txt', 'a') as log_file:
            log_file.write(f'Cleanup complete at {datetime.datetime.now()}\n')

        time.sleep(86400)  # Подождать 24 часа (или другой интервал) перед следующей очисткой





