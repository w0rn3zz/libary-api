# 📚 Library API

Этот репозиторий содержит реализацию тестового задания: RESTful API для базового управления библиотечным каталогом.

## 📋 Краткое описание задания

Необходимо разработать API, который позволяет:

- Управлять книгами и читателями (CRUD-операции);
- Реализовать выдачу и возврат книг с бизнес-ограничениями (максимум 3 книги на читателя, учёт экземпляров и возвратов);
- Добавить регистрацию и аутентификацию библиотекарей с использованием JWT токенов;
- Обеспечить защиту всех ключевых операций через токен.

## 🛠️ Технологии

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Alembic
- Pydantic
- Pytest
- Docker

## 📂 Структура проекта (будет обновляться)
```
library-api
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
├── docker/
│   ├── scripts/
│   │   └── init.sh
│   └── volumes/
│       └── db-data/
│           └── .gitkeep
├── src/
│   ├── main.py
│   ├── database.py               # db connection related 
│   ├── exceptions.py             # global exceptions
│   ├── dao/
│   │   └── base.py
│   ├── config/
│   │   ├── app.py                # app-wide config
│   │   ├── base.py               # config logic
│   │   └── database.py           # DB URL config
│   ├── books/
│   │   ├── models.py             # db models
│   │   └── router.py             # endpoints
│   ├── borrows/
│   │   └── models.py
│   ├── readers/
│   │   └── models.py
│   └── users/
│       ├── auth.py               # auth logic
│       ├── dao.py                # user queries
│       ├── dependencies.py
│       ├── models.py             # db models
│       ├── router.py             # endpoints
│       └── schemas.py            # pydantic models
├── .env
├── .env-docker
├── .gitignore
├── README.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini

```
## 🚧 Статус

- Добавлены базовые модели (Book, Reader, Borrow, User)
- Реализованы эндпоинты для JWT авторизации

В ближайшее время будет реализовано управление книгами


## 👤 Автор

w0rn3zz

📅 Начало разработки: 19.06.2025

