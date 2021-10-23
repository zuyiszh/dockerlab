FROM centos  # 调用docker中已下载的centos镜像
MAINTAINER FeiYi  # 作者名为FeiYi
# 安装环境所需包
RUN yum -y install net-tools iproute pcre-devel openssl-devel gcc gcc-c++ make zlib-devel elinks
ADD nginx-1.18.0.tar.gz /usr/src  # 解压本地host中的nginx包到容器中的/usr/src目录
ENV NGINX_DIR /usr/src/nginx-1.18.0 # 定义环境变量
WORKDIR $NGINX_DIR  # 进入容器中的解压目录
# 编译安装
RUN ./configure --prefix=/usr/local/nginx --user=nginx --group=nginx && make && make install
# 回到根目录
WORKDIR /
# 创建程序用户
RUN useradd nginx
# 优化命令环境
RUN ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx
# 监听端口80
EXPOSE 80
# 后台启动nginx服务
CMD ["nginx", "-g", "daemon off;"]
