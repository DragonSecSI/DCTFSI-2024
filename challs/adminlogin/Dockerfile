FROM ubuntu:20.04
RUN apt-get update && apt-get install -y make gcc socat

RUN groupadd pilot
RUN useradd pilot --gid pilot

COPY ./app /app
WORKDIR /app
RUN chmod a=r *

EXPOSE 5555

ENTRYPOINT [ "bash", "start.sh" ]
