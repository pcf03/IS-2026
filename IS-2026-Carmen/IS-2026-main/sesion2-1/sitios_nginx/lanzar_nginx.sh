#!/bin/sh

docker run --rm \
    -p 80:80 \
    -p 81:81 \
    -v "$(pwd)/default.conf:/etc/nginx/conf.d/default.conf:ro" \
    -v "$(pwd)/sitio2.conf:/etc/nginx/conf.d/sitio2.conf:ro" \
    -v "$(pwd)/html:/usr/share/nginx/html:ro" \
    -v "$(pwd)/html2:/usr/share/nginx/html2:ro" \
    nginx