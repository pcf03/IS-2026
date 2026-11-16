#!/bin/bash
docker run -d --rm --name prometheus \
  --network pruebas \
  -p 9090:9090 \
  -v $(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus