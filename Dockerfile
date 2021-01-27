FROM python:3.9

COPY src /srv/tubemap
WORKDIR /srv/tubemap

RUN pip3 install -r requirements.txt

RUN wget -O d3-tube-map.zip https://github.com/johnwalley/d3-tube-map/archive/v1.5.0.zip \
    && unzip d3-tube-map.zip -d js

ENV FLASK_APP=tubemap.py
ENV FLASK_ENV=development

ENTRYPOINT [ "flask" ]