# pull official base image
FROM python:3.11

# maintainers info
LABEL maintainer="amir.maalehmir@gmail.com"

# set work directory
WORKDIR /code

# install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt 

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /code/

# collecting static files
RUN python manage.py collectstatic --no-input