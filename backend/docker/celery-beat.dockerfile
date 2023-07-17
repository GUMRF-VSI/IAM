FROM python:3.11-slim-bullseye

# Устанавливаем рабочие дерикторию
WORKDIR /app

# Устанавливем nano для работы с файлыми внутри контейнера (необязательно)
RUN apt-get update \
 && apt-get install -y -qq --no-install-recommends curl nano iputils-ping ethtool tcpdump jq git \
 && apt-get clean && rm -rf /var/lib/apt/lists/* \
 && pip install poetry

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем исходные файлы
COPY . /app

# Копируем скрипт для запуска проекта
RUN cp script/celery-beat.sh ./ && chmod +x ./celery-beat.sh

# Запускаем проект
CMD ["/app/celery-beat.sh"]
