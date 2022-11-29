FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN apk add --no-cache mariadb-connector-c-dev
# RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
