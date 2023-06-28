# Работа с миграциями

---

## Создание миграций

### Автоматическая генерация миграций 

```shell
alembic revision --autogenerate -m '<migration name>'
```

---

## Применение конкретной миграции

Для применения конкретной миграции необходимо после `upgrade` указать `revision` миграции, значение которой находится в 
файле необходимой миграции в директории `migration/versions/...`.

```shell
alembic upgrade <migration revision>
```

### Пример

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

---

## Применение последних миграций

```shell
alembic upgrade head
```

---

## Откат конкретной миграции

Для применения конкретной миграции необходимо после `upgrade` указать `revision` миграции, значение которой находится в 
файле необходимой миграции в директории `migration/versions/...`.

```shell
alembic downgrade <migration revision>
```

### Пример

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

---

## Откат всех миграций

```shell
alembic downgrade base
```
