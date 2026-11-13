#!/bin/bash
# Crear la subred pruebas (el '|| true' evita que falle si ya existe)
docker network create pruebas || true

echo "Lanzando 3 servidores broadcast en background..."
docker run -d --rm --name servidor_broadcast_1 --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py
docker run -d --rm --name servidor_broadcast_2 --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py
docker run -d --rm --name servidor_broadcast_3 --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py

echo "Servidores en ejecución. Usa 'docker ps' para verlos."