docker run --name qyt-psql \
           --network psql-net \
           -v /docker_compose_swarm/docker_1_Dockerfile_3_nginx_django_psql/psql/init-user-db.sh:/docker-entrypoint-initdb.d/init-user-db.sh \
           -e POSTGRES_PASSWORD=Cisc0123 \
           -d postgres
