FROM python:3.9

COPY src /srv/tubemap
WORKDIR /srv/tubemap

RUN pip3 install -r requirements.txt

ENV FLASK_APP=tubemap.py
ENV FLASK_ENV=development

ENTRYPOINT [ "flask" ]