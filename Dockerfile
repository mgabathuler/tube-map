FROM python:3.9

COPY src /srv
WORKDIR /srv

RUN pip3 install -r requirements.txt

RUN wget -O d3-tube-map.zip https://github.com/johnwalley/d3-tube-map/releases/download/v1.5.0/d3-tube-map.zip \
    && unzip d3-tube-map.zip -d tubemap/FlaskApp/static/tubemap \
    && rm -f d3-tube-map.zip

ENV FLASK_APP=tubemap.py
ENV FLASK_ENV=development

ENTRYPOINT [ "python" ]