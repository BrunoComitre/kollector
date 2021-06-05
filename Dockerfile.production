FROM python:3.9.5-slim-buster

# work directory
WORKDIR /usr/app

# Impede o Python grave arquivos pyc no disco(equivale à python -B option)
ENV PYTHONDONWRITEBYCODE 1

# Impede o Python armazene em buffer stdout/stderr(equivale à python -u option)
ENV PYTHONUNBUFFERED 1

COPY ./requirements/ /usr/requirements/

COPY ./requirements.txt /usr/requirements.txt

RUN pip install --upgrade pip

RUN apt-get update \
  && pip install -r /usr/requirements.txt

COPY . /usr/app/
