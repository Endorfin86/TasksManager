# Базовый образ
FROM python:3.9

# Объявляем переменную окружения для установки режима дебага
ENV DEBUG 0

RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Указываем рабочую директорию в контейнере
WORKDIR /code

# Копируем файлы проекта в контейнер
COPY . /code/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt


# Устанавливаем локали в контейнер (если необходимо)
RUN apt-get update && apt-get install -y locales locales-all
RUN locale-gen ru_RU.UTF-8
RUN echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen
ENV LANG ru_RU.UTF-8


# Открываем порт 8000
EXPOSE 8000

# Запускаем сервер Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]