FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt 
CMD python manage.py migrate \
    && echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@heptracapital.com', '1234')" | python manage.py shell \
    && python manage.py runserver 0.0.0.0:8080


