FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd && apk add -u gcc musl-dev

RUN pip install -r requirements.txt

COPY .docker/wait.sh /wait.sh
RUN chmod +x /wait.sh
