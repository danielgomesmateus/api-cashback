FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/code

WORKDIR /app/code/

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
python3-dev

RUN pip install --upgrade pip

COPY requirements.txt /app/code/

RUN pip install -r /app/code/requirements.txt

ADD . /app/code/