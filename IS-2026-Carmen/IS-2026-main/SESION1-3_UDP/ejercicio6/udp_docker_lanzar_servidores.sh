#!/bin/bash

docker run -d --name servidor1 --network pruebas \
-v $(pwd):/app python:3.7 \
python /app/udp_servidor6_broadcast.py

docker run -d --name servidor2 --network pruebas \
-v $(pwd):/app python:3.7 \
python /app/udp_servidor6_broadcast.py

docker run -d --name servidor3 --network pruebas \
-v $(pwd):/app python:3.7 \
python /app/udp_servidor6_broadcast.py

# poner esto para eleminar los ya creados porque si no no crea mas
# docker rm -f servidor1 servidor2 servidor3 cliente