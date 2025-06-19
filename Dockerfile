FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

ENV PYTHONUNBUFFERED=1