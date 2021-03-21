FROM python:3.7-alpine

LABEL maintainer="srbarrios@gmail.com"

RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install --upgrade pip \
  && pip install cython

COPY ./web/requirements.txt /requirements.txt

RUN pip --no-cache-dir install -r /requirements.txt

ENV APP_ROOT '/application'
RUN mkdir -p $APP_ROOT

WORKDIR $APP_ROOT
COPY ./web/ $APP_ROOT

EXPOSE 5000

ENTRYPOINT gunicorn \
        --access-logfile="-"                   \
        --error-logfile="-"                    \
        --bind=0.0.0.0:5000                    \
        --worker-class=sync                    \
        --workers=1                            \
        --keep-alive=10                        \
        --graceful-timeout=10                  \
        app:app



