FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=ms
ENV FLASK_ENV=development

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD flask run --host=0.0.0.0
