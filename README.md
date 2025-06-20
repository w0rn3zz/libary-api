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
│ 
├── docker/
│   ├── scripts/
│   │   └── init.sh
│   └── volumes/
│       └── db-data/
│           └── .gitkeep
├── src/
│   ├── main.py
│   ├── database.py
│   ├── exceptions.py
│   ├── dao/
│   │   └── base.py
│   ├── config/
│   │   ├── app.py
│   │   ├── base.py
│   │   └── database.py
│   ├── books/
│   │   ├── models.py
│   │   ├── router.py
│   │   └── schemas.py
│   ├── borrows/
│   │   └── models.py
│   ├── readers/
│   │   └── models.py
│   └── users/
│       ├── auth.py
│       ├── dao.py
│       ├── dependencies.py
│       ├── models.py
│       ├── router.py
│       └── schemas.py
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
- Реализовано управление книгами, защищено JWT(CRUD)

В ближайшее время будет реализовано управление читателями


## 👤 Автор

w0rn3zz

📅 Начало разработки: 19.06.2025

