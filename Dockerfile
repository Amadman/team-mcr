FROM jfloff/alpine-python:3.6-onbuild

RUN adduser -D mcr

WORKDIR /home/mcr

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN apk add --update nodejs nodejs-npm

COPY app app
COPY mcr.py config.py boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP mcr.py

RUN chown -R mcr:mcr ./
USER mcr

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
