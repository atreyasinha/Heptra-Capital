FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt 
CMD python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8080


