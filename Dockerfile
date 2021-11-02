FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=ms
ENV FLASK_ENV=development

RUN apk update \
    && apk add --no-cache \
        build-base \
        postgresql-dev	\
        python3-dev

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

EXPOSE 5000
CMD flask run --host=0.0.0.0
