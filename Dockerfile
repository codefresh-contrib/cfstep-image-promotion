FROM python:3.6.4-alpine3.7

ENV LANG C.UTF-8

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
        git \
        nodejs && \
    pip install requests && \
    npm install codefresh -g

COPY lib/promote.py /promote.py

ENTRYPOINT ["python", "/promote.py"]