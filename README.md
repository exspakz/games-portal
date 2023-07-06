# [Django Games Portal](http://127.0.0.1:8000/)


## Содержание

[1. Описание проекта](README.md#Описание-проекта)  
[2. Функционал](README.md#Функционал)  
[3. Установка и запуск](README.md#Установка-и-запуск)  


## Описание проекта

В рамках проекта был реализован информационный интернет-ресурс для фанатского сервера MMORPG — что-то вроде доски объявлений, который может послужить прототипом для других аналогичных проектов. В данном случае - для фанатов игры MMORPG.
В проекте реализована возможность размещения категоризированных объявлений и комментариев к ним для зарегистрированных пользователей. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. На каждый комментарий автор объявления может реагировать - принимать, отклонять и сбрасывать статус.

:arrow_up: [к содержанию](README.md#Содержание)


## Функционал

#### Реализация и используемые технологии:

- фреймворк Django
- хранение данных - SQLite
- регистрация/авторизация через email или социальные сети - библиотека allauth
- асинхронное выполнение задач по e-mail рассылке - Celery + Redis
- встроенный WYSIWYG-редактор - CKEditor

#### Действующие e-mail оповещения-рассылки, выполняются асинхронно:

- приветствие при регистрации и подтверждении аккаунта
- размещение нового отклика для объявления его автору
- публикацию статьи в новостной ленте

:arrow_up: [к содержанию](README.md#Содержание)


## Установка и запуск

#### Клонируйте проект с GitHub локально и перейдите в папку `games-portal`:

```bash
git clone https://github.com/Exspakz/games-portal.git
cd games-portal
```

#### Создайте виртуальное окружение для проекта:

```bash
python -m venv venv_games_portal
source venv_games_portal/bin/activate
```

#### Установите необходимые пакеты из файла `games_portal/requirements.txt`:
```bash
pip install -r games_portal/requirements.txt 
```

#### Сгенерировать секретный ключ Django:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Отправка e-mail писем происходит с помощью сервиса Yandex.

Для настройки выполните Шаг 1 и Шаг 2 по инструкции: [Настроить программу по протоколу IMAP](https://yandex.ru/support/mail/mail-clients/others.html). Сохраните пароль приложения - он понадобится на следующем шаге.


#### В файле `games_portal/.env.Example` замените шаблонные переменные окружения:

```python
# django
SECRET_KEY = 'SECRET_KEY'

# yandex api
EMAIL = 'DEFAULT_FROM_EMAIL'
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
PASSWORD_API = 'EMAIL_HOST_PASSWORD'
```

#### Установите сервер Redis локально в вашей операционной системе:

```bash
sudo apt-get update  
sudo apt-get install redis  
```

#### Или подключите через облачную базу данных Redis, тогда в файле `games_portal/.env.Example` замените переменные окружения:

```python
# celery
USERNAME_REDIS = 'USERNAME_REDIS'
PASSWORD_REDIS = 'PASSWORD_REDIS'
ENDPOINT = 'ENDPOINT'
```

#### Создайте и примените миграции из каталога проекта */newspaper/*:
```bash
python manage.py makemigrations 
python manage.py migrate 
```

#### Запуск проекта, выполните команды в отдельных консольных окнах:

 - `redis-server` - сервер Redis, если он установлен локально  
 - `celery -A games_portal worker -l INFO -B` - Celery из каталога проекта */games_portal/*
 - `python manage.py runserver` - запуск Django-проекта из каталога проекта */games_portal/*

:arrow_up: [к содержанию](README.md#Содержание)