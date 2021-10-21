docker build -t collinsctk/django .

docker run --name qyt-django --network psql-net -d collinsctk/django

docker network connect django-net qyt-django