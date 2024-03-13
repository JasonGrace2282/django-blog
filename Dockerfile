FROM ubuntu:22.04

ENV TZ "America/New_York"

RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y python3 python3-pip git

COPY requirements.txt .

RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime\
  && pip3 install -Ir requirements.txt\
  && rm requirements.txt


WORKDIR /sysblog
