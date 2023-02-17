FROM python:3.11.1-alpine3.17

RUN echo "https://dl-4.alpinelinux.org/alpine/v3.17/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories


# Setup
RUN apk update
RUN apk upgrade
#RUN apk add --update --no-cache python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN apk add --update --no-cache postgresql-client postgresql-dev build-base gettext
RUN apk add --update --no-cache py3-pip bash
RUN apk add --update --no-cache curl lftp

# Clean
RUN apk add --update --no-cache openssh
RUN rm -fr /var/cache/apk/*
#
# Initialize
RUN mkdir -p /data/backend
RUN mkdir -p /opt/persistent
WORKDIR /data/backend
#
# Prepare
COPY ./manage.py /data/backend/
COPY ./landlord /data/backend/landlord
COPY ./theperfectlandlord /data/backend/theperfectlandlord
COPY ./static/ /data/backend/static
COPY requirements.txt /data/backend/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./static/admin /data/backend/static/admin

#COPY --from=ffmpeg /usr/local /usr/local