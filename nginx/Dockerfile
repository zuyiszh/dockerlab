FROM centos:8
RUN yum -y update && yum -y install vim net-tools && yum install -y epel-release && yum -y install nginx
LABEL maintainer="Qin Ke<collinsctk@qytang.com>"

ADD static /qytdjg/static/
ADD nginx.conf /etc/nginx/nginx.conf

CMD nginx
