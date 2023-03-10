FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY django.conf /etc/nginx/conf.d/

RUN apk update
RUN apk upgrade
RUN apk add --update --no-cache busybox-extras bash

RUN mkdir -p /data/nginx/html
RUN mkdir -p /opt/theperfectlandlord/website/
COPY self_sign_cert/nginx-selfsigned.crt /data/nginx/
COPY self_sign_cert/nginx-selfsigned.key /data/nginx/
COPY html/ /data/nginx/html
RUN chown -R nginx.nginx /data/nginx
