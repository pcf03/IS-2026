#!/bin/bash

docker run --rm -d \
    --network pruebas \
    --name nginx \
    --add-host=host.docker.internal:host-gateway \
    -p 80:80 \
    -p 81:81 \
    -v "$(pwd)/html:/usr/share/nginx/html" \
    -v "$(pwd)/html2:/usr/share/nginx/html2" \
    -v "$(pwd)/sitios_nginx:/etc/nginx/conf.d" \
    nginx
