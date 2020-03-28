FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate
