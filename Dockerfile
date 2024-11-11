FROM python:3.12.3

LABEL authors="ahmadbinshafiq"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements /tmp
WORKDIR /tmp

RUN pip install -r local.txt

WORKDIR /app
