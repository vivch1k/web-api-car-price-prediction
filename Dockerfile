# Используем официальный образ Python как базовый
FROM python:3.9-slim

# Устанавливаем необходимые пакеты для psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения в контейнер
COPY . .

# Объявляем переменные окружения, если они нужны
ENV SOME_ENV_VAR=default_value

# Открываем порт, который будет слушать приложение
EXPOSE 8000

# Команда для запуска приложения через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
