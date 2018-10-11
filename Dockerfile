FROM ubuntu:16.04

RUN apt-get update

RUN apt install -y python3-pip && \
    pip3 install --upgrade setuptools

WORKDIR /gateway

ADD ./requirements.txt /gateway/requirements.txt

RUN pip3 install -r requirements.txt

RUN apt-get install -y libgtk2.0-dev

ADD ./gateway /gateway/

CMD python3 stream.py
# CMD [python3 stream.py]