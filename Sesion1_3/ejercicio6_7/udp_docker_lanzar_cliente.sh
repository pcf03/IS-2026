#!/bin/bash
IP_BROADCAST=$1

if [ -z "$IP_BROADCAST" ]; then
    echo "ERROR: Falta la IP de broadcast."
    echo "Uso: ./udp_docker_lanzar_cliente.sh <IP_BROADCAST>"
    exit 1
fi

echo "Lanzando cliente buscando en la IP de broadcast: $IP_BROADCAST"
docker run -it --rm --name cliente_broadcast --network pruebas -v $(pwd):/app python:3.7 python /app/udp_cliente6_broadcast.py "$IP_BROADCAST"