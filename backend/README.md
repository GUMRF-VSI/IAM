# Auth Backend

---

* [Запуск проекта для локальной разработки](#запуск-проекта-для-локальной-разработки)
  * [Запуск при помощи Dokcer](#запуск-при-помощи-dokcer)
    * [Опционально](#опционально)
* [Работа с миграциями](#работа-с-миграциями)
  * [Инициализация миграций](#инициализация-миграций)
  * [Настройка скрипта](#настройка-скрипта)

---

## Запуск проекта для локальной разработки

### Запуск при помощи Dokcer
1. Перейти в директорию `./docker`
2. Создать файл `.env` и скопировать туда значение из `.env.template`
3. Запустить контейнер `docker-compose up`

#### Опционально

Для создания таблиц и применения миграций следовать [инструкции](#применение-последних-миграций).

---

## Работа с миграциями

Информацию о создании миграций и работе с ними можно найти [тут](./app/database/models/migrations/README.md)

### Инициализация миграций

Для того чтобы инициализировать скрипт создания миграций, нужно выполнить команду.

```shell
alembic init <желаемое расположение миграций>/migrations
```

### Настройка скрипта

Для корректной работы миграций, необходима настройка скрипта создания миграций. Сначала нужно настроить `alembic.ini`. 
В файле нужно заменить строку `sqlalchemy.url = driver://user:pass@localhost/dbname` на 
`sqlalchemy.url = <dialect>://%(<USER>)s:%(<PASSWORD>)s@%(<HOST>)s/%(<DB>)s`, где dialect - используемая база данных,
USER, PASSWORD, HOST, DB - данные для подключения к БД.

После чего нужно настроить файл `<желаемое расположение миграций>/migrations/env.py`. 

Добавить импорт и использование класса Base из файла моделей. 

```python
...
from database.models.models import Base
...
target_metadata = Base.metadata
...
```

```python
from alembic import context

from <ваш файл настроект> import settings

config = context.config

section = config.config_ini_section
config.set_section_option(section, 'POSTGRES_USER', settings.USER)
config.set_section_option(section, 'POSTGRES_PASSWORD', settings.PASSWORD)
config.set_section_option(section, 'POSTGRES_HOST', settings.DB_HOST)
config.set_section_option(section, 'POSTGRES_PORT', settings.PORT)
config.set_section_option(section, 'POSTGRES_DB', settings.DB)
```

#### Важно

1. Необходимо использовать для настроек `pydantic.BaseSettings`
2. Для создания миграций в качестве `DB_HOST` нужно использовать внешний порт для подключения базы данных. 