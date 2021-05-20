FROM python:3.8.9-buster

WORKDIR /app

ADD . /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
