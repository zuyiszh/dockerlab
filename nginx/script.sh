docker build -t collinsctk/nginx .

docker run --name qyt-nginx --network nginx-net -p 80:80 -d collinsctk/nginx

docker network connect django-net qyt-nginx

docker restart qyt-nginx