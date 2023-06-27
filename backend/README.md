# Auth Backend

---

* [Запуск проекта для локальной разработки](#запуск-проекта-для-локальной-разработки)
  * [Запуск при помощи Dokcer](#запуск-при-помощи-dokcer)
    * [Опционально](#опционально)
* [Работа с миграциями](#работа-с-миграциями)
  * [Применение конкретной миграции](#откат-конкретной-миграции)
  * [Применение последних миграций](#применение-последних-миграций)
  * [Откат конкретной миграции](#откат-конкретной-миграции)
  * [Откат всех миграций](#откат-всех-миграций)

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

### Создание миграций

#### Автоматическая генерация миграций 

```shell
alembic revision --autogenerate -m '<migration name>'
```

### Применение конкретной миграции

Для применения конкретной миграции необходимо после `upgrade` указать `revision` миграции, значение которой находится в 
файле необходимой миграции в директории `migration/versions/...`.

```shell
alembic upgrade <migration revision>
```

#### Пример

`./migration/versions/1a2b34cd5e67.py`

```python
...
# revision identifiers, used by Alembic.
revision = '1a2b34cd5e67'
down_revision = None
branch_labels = None
depends_on = None
...
```

```shell
alembic upgrade 1a2b34cd5e67
```

### Применение последних миграций

```shell
alembic upgrade head
```

### Откат конкретной миграции

Для применения конкретной миграции необходимо после `upgrade` указать `revision` миграции, значение которой находится в 
файле необходимой миграции в директории `migration/versions/...`.

```shell
alembic downgrade <migration revision>
```

#### Пример

`./migration/versions/1a2b34cd5e67.py`

```python
...
# revision identifiers, used by Alembic.
revision = '1a2b34cd5e67'
down_revision = None
branch_labels = None
depends_on = None
...
```

```shell
alembic downgrade 1a2b34cd5e67
```

### Откат всех миграций

```shell
alembic downgrade base
```