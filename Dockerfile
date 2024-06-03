FROM python:3.11-alpine

ENV DJANGO_ENV=production

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip -install -r requirements.txt

WORKDIR /app/registration

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]