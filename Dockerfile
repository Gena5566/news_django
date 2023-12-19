# Образ Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все содержимое текущей директории внутрь контейнера
COPY . /app/

# Определяем переменные окружения
ENV PYTHONUNBUFFERED 1

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем команду при запуске контейнера
CMD ["python", "mynewsproject/manage.py", "runserver", "0.0.0.0:8000"]

