#Owl TicketSelling Dockerfile
#version 1.0
#Author: liziqiao
#Base image
FROM liziqiao/owl
#MAINTAINER
MAINTAINER 1240148677@qq.com
#WORKDIR
WORKDIR /usr/src/owl
RUN rm -rf TicketSelling
WORKDIR /usr/src/owl
RUN git clone https://github.com/Owl-Movies-Ticket-System/TicketSelling
WORKDIR /usr/src/owl/TicketSelling
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
#EXPOSE
EXPOSE 8000