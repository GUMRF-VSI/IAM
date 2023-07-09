FROM python:3.11-slim-bullseye

# Устанавливаем рабочие дерикторию
WORKDIR /app

# Копируем файлы зависимостей
COPY ../requirements.txt ./requirements.txt

# Устанавливем nano для работы с файлыми внутри контейнера (необязательно)
RUN apt-get update \
 && apt-get install -y -qq --no-install-recommends curl nano iputils-ping ethtool tcpdump jq git \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
RUN python -m pip install pip --upgrade \
 && python -m pip install -r requirements.txt

# Копируем исходные файлы
COPY . /app

# Копируем скрипт для запуска проекта
RUN cp script/entrypoint.sh ./ && chmod +x ./entrypoint.sh

# Создаем пользователя
RUN groupadd --gid 1001 app \
  && useradd --uid 1001 --gid app --shell /bin/bash app

# Даем пользователю полные права (для работы с файлыми внутри контейнера через пользователя)
RUN chgrp -R app /app
RUN chmod -R 770 /app

# Используем созданного пользователя
USER app

# Запускаем проект
CMD ["/app/entrypoint.sh"]
