FROM python:3.9-alpine

WORKDIR /app

COPY chall/requirements.txt /app
RUN pip install -r requirements.txt

COPY chall/app.py /app
COPY chall/templates /app/templates
COPY chall/static /app/static
ENV FLAG DCTF{p4ck3d_7h3_fl4g_10_7h3_m00n}

EXPOSE 8000
CMD python ./app.py
