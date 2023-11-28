# product shop project

## Описание проекта

Проект магазина продуктов

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Документация

Документация находится по ссылкам:
1. Swagger `api/schema/swagger-ui/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. Cклонируйте репозиторий себе на компьютер
2. Установите необходимые зависимости командой `poetry install`
3. Создайте БД
4. Создайте файл .env и заполните его, используя образец из файла .env.example
5. Выполните миграции командой `python manage.py migrate`
6. Выполните команду `python manage.py fill_db`

## Файл .env.example

1. `POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `SECRET_KEY, DEBUG, ALLOWED_HOSTS`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
