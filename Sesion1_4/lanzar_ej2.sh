docker run -d --rm -p 9091:9999 --network uo287992 --name servidor_tcp -v $(pwd):/app python:3.7 python /app/tcp_servidor6_oche_len.py 9999 
