FROM python:3-alpine

MAINTAINER Yehuda Deutsch <yeh@uda.co.il>

RUN apk update && apk add gcc musl-dev postgresql-dev jpeg-dev zlib-dev && pip install pipenv

COPY Pipfile Pipfile
RUN pipenv install --deploy --system --skip-lock

COPY bower.json /tmp/bower.json
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g bower \
    && cd /tmp \
    && bower --allow-root -F install

WORKDIR /app
COPY . /app
RUN mv /tmp/bower_components /app/bower_components

CMD ["make", "run"]
