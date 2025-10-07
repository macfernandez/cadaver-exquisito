FROM ubuntu:24.04

# use env and delete this
ENV PIP_BREAK_SYSTEM_PACKAGES 1

WORKDIR /root

RUN apt-get update \
    && apt-get install -y python3 python3-venv python3-pip

RUN apt update \
    && apt install --only-upgrade -y python3-pip

RUN pip install setuptools
