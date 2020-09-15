FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-pyqt5 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip \
    && pip3 install opencv-python \
    && rm -rf ~/.cache/pip

WORKDIR /workspace
COPY main.py main.py

CMD python3 main.py
