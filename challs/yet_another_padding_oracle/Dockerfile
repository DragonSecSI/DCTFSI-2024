FROM python:3.11.9-slim

WORKDIR /app

RUN pip install pycryptodome


RUN apt-get -y update && \
    apt-get -y install socat coreutils

COPY ./chall/chall.py .
COPY ./chall/flag.txt .

RUN chmod 555 /app/chall.py

EXPOSE 1337

CMD socat -T 30 \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 python /app/chall.py"