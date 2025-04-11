FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get install -y libpq-dev gcc
RUN pip install -r requirements.txt

COPY . .