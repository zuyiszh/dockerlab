FROM centos:8
RUN yum -y install net-tools iproute pcre-devel openssl-devel gcc gcc-c++ make zlib-devel
ADD nginx-1.18.0.tar.gz /usr/src
ENV NGINX_DIR /usr/src/nginx-1.18.0
WORKDIR $NGINX_DIR
RUN ./configure --prefix=/usr/local/nginx --user=nginx --group=nginx && make && make install
WORKDIR /
RUN useradd nginx
RUN ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
