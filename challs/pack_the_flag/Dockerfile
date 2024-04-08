FROM python:3.9-alpine

WORKDIR /app

COPY chall/requirements.txt /app
RUN pip install -r requirements.txt

COPY chall/app.py /app
COPY chall/templates /app/templates
COPY chall/static /app/static

EXPOSE 8000
CMD python ./app.py
