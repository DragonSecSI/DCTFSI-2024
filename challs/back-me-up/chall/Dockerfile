FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY backmeup/ /app/backmeup

EXPOSE 8000
CMD python -m backmeup
