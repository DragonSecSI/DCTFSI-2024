FROM ubuntu:20.04
RUN RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y socat

RUN groupadd pilot
RUN useradd pilot --gid pilot

COPY ./app /app
WORKDIR /app
EXPOSE 5555

ENTRYPOINT [ "bash", "start.sh" ]
