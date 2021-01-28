FROM python:3.7

COPY requirements.txt /srv/requirements.txt

WORKDIR /srv
RUN pip3 install -r requirements.txt