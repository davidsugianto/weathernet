FROM python:3-alpine AS builder

LABEL maintainer David Sugianto <idiots718@gmail.com>

WORKDIR /app/jcli

COPY . ./

RUN apk update --no-cache && \
    apk add --no-cache gcc g++ libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev libstdc++ tzdata && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python" ]