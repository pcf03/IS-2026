sudo apt update
sudo apt upgrade
sudo addgroup --system docker
sudo adduser uo287992 docker
sudo snap install docker
logout
ifconfig
sudo systemctl restart ssh
sudo systemctl status ssh
ifconfig
poweroff
sudo poweroff
git clone https://github.com/pcf03/IS-2026.git
cd IS-2026/Sesion1_3/ejercicio4
python3 udp_cliente4_reintenta.py
ls
cd IS-2026/
ls
mkdir Sesion1_3
ls
mv ejercicio1 ejercicio2 ejercicio3 Sesion1_3/
ls
cd Sesion1_3/
ls
cd ejercicio
cd ejercicio1
ls
cd ..
git add .
git commit -m "Mover carpetas de ejercicios a Sesion1_3"
git config --global user.email "paulacortinaferrero@gmail.com"
git config --global user.name "pcf03"
git push
ls
clear
cd Sesion1_3/
cd ejercicio3
python3 udp_servidor3_con_ok.py 9999
ls
python3 udp_servidor3_con_ok.py 9999
clear
python3 udp_servidor3_con_ok.py
cd ..
clear
python3 udp_servidor3_con_ok.py 9999
python3 ejercicio3/udp_servidor3_con_ok.py 
ls
cd ejercicio3
ls
pyhon3  udp_servidor3_con_ok.py
python3  udp_servidor3_con_ok.py
clear
mv ' udp_servidor3_con_ok.py' udp_servidor3_con_ok.py
mv ' udp_cliente3_espera_ok.py' udp_cliente3_espera_ok.py
ls
python3 udp_servidor3_con_ok.py
ls
cd IS-2026/Sesion1_3/
docker pull python:3.7
cd ..
docker pull python:3.7
sudo snap install docker
sudo adduser uo287992 docker
exit
cd IS-2026/
docker pull python:3.7
cd ~/IS-2026/Sesion1_3
docker run -d --rm --name servidor1 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor2 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor3 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run --rm -it --name cliente -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_cliente6_broadcast.py
docker network create pruebas
docker run -d --rm --name servidor1 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor2 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor3 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run --rm -it --name cliente -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_cliente6_broadcast.py
clear
docker run -d --rm --name servidor1 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor2 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor3 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run --rm -it --name cliente -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_cliente6_broadcast.py
cd ejercicio6_7/
clear
docker run -d --rm --name servidor1 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor2 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run -d --rm --name servidor3 -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_servidor6_broadcast.py
docker run --rm -it --name cliente -v ${PWD}:/app -w /app --network pruebas python:3.7 python3 udp_cliente6_broadcast.py
clear
cd ..
git add .
git commit -m "Completados Ejercicios 6 y 7 de broadcast con Docker"
git push
ifconfig
sudo shutdown now
python3 tcp_cliente5_oche_readline.py localhost 9090
cd Sesion1_4
cd ejercicio6
python3 tcp_cliente5_oche_readline.py localhost 9090
cd ..
cd ejercicio5
python3 tcp_cliente5_oche_readline.py localhost 9090
cd Sesion2_1
ls
docker build -t gunicornflask:1.0 .
cd flask/
docker build -t gunicornflask:1.0 .ç
docker build -t gunicornflask:1.0 .
cd ..
chmod +x lanzar_flask.sh
chmod +x lanzar_mariadb.sh
clear
./lanzar_mariadb.sh
./lanzar_flask.sh
./lanzar_nginx.sh
clear
cd ..
cd Sesion1_4
ls
cd ejercicio6
ls
docker run -d --rm -p 9090:9999 --network pruebas   --name servidor_oche -v $(pwd):/app   python:3.7 python /app/tcp_servidor5_oche_readline.py
clear
cd ..
cd ejercicio5
docker run -d --rm -p 9090:9999 --network pruebas   --name servidor_oche -v $(pwd):/app   python:3.7 python /app/tcp_servidor5_oche_readline.py
ifconfig
git --version
cd ~
git clone https://github.com/pcf03/IS-2026.git
ls
cd IS-2026/
ls
git status
git remote -v
git pull
python3 udp_cliente5_mejorado.py 127.0.0.1 9999
cd Sesion1_3
cd ejercicio5
python3 udp_servidor5_mejorado.py 9999
clear
git add .
git commit -m "Completado Ejercicio 5: Implementado protocolo UDP robusto con identificadores unicos y filtrado de duplicados"
git push
clear
cd ..
cd ejercicio6_7/
clear
chmod +x udp_docker_lanzar_servidores.sh udp_docker_lanzar_cliente.sh
./udp_docker_lanzar_servidores.sh 
docker inspect servidor_broadcast_1 | grep IPAddres
./udp_docker_lanzar_cliente.sh 172.18.0.2
git add .
git commit -m "Terminada Sesion 1.3: Implementado ejercicio 7, servicios broadcast usando docker"
git push
clear
ip a
ls /etc/netplan
sudo nano /etc/netplan/50-cloud-init.yaml 
clear
sudo netplan try
ip a
cd Sesion2_2
ls
docker run --name basedatos   -e MYSQL_ROOT_PASSWORD=claveroot   -e MYSQL_USER=amigosuser   -e MYSQL_DATABASE=amigosdb   -e MYSQL_PASSWORD=amigospass   -v $(pwd)/basedatos:/var/lib/mysql   --rm --network pruebas -d mariadb
docker inspect basedatos | grep IPAddress
cd amigos/
ls
FLASK_APP=lanzar.py flask run -h 0.0.0.0
sudo apt install python3-flask
FLASK_APP=lanzar.py flask run -h 0.0.0.0
source ~/flaskenv/bin/activate
export DEPLOYMENT_MODE=development
FLASK_APP=lanzar.py flask run -h 0.0.0.0
clear
FLASK_APP=lanzar.py flask db migrate -m "Crear tabla amigos"
FLASK_APP=lanzar.py flask db init
FLASK_APP=lanzar.py flask db migrate -m "Creacion inicial tabla amigos"
FLASK_APP=lanzar.py flask db upgrade
FLASK_APP=lanzar.py flask run -h 0.0.0.0
exit
cd Sesion2_2
cd amigos/
docker build -t amigos:1.0 .
docker images
clear
cd ..
mkdir sitios_nginx
nano sitios_nginx/default.conf
nano lanza-basedatos.sh
nano lanza-flask.sh
nano lanza-nginx.sh
chmod +x lanza-basedatos.sh lanza-flask.sh lanza-nginx.sh
docker stop basedatos
./lanza-basedatos.sh
./lanza-flask.sh
./lanza-nginx.sh
uo287992@is-16:~/IS-2026/Sesion2_2$ ./lanza-nginx.sh
./lanza-nginx.sh 
docker ps
docker logs nginx
curl http://127.0.0.1/html/amigos
clear
docker stop nginx amigos basedatos
./lanza-basedatos.sh
cd amigos/
source ~/flaskenv/bin/activate
FLASK_APP=lanzar.py flask db migrate -m "Añadido campo device a amigos"
FLASK_APP=lanzar.py flask db upgrade
clear
docker build -t amigos:2.0 .
docker rm -f nginx amigos basedatos 2>/dev/null
--rm -d --network pruebas amigos:2.0
clear
./lanza-basedatos.sh
./lanza-flask.sh
./lanza-nginx.sh
cd ..
clear
./lanza-basedatos.sh
./lanza-flask.sh
./lanza-nginx.sh
docker ps
curl http://127.0.0.1/html/amigos
curl -X POST http://127.0.0.1/api/amigos      -H "Content-Type: application/json"      -d '{"name": "Manolo", "lati": "43.5", "longi": "-5.6", "device": "Pixel 7"}'
curl http://127.0.0.1/api/devices
clear
docker build -t amigos:2.0 .
cd amigos
clear
docker stop amigos
./lanza-flask.sh
docker stop amigos
cd ..
./lanza-flask.sh 
curl -X POST http://127.0.0.1/api/amigos      -H "Content-Type: application/json"      -d '{"name": "Manolo", "lati": "43.5", "longi": "-5.6", "device": "Pixel 7"}'
clear
cd amigos/
docker stop nginx amigos 2>/dev/null
cd ~/IS-2026/Sesion2_2/amigos
docker build -t amigos:2.0 .
cd ..
./lanza-flask.sh
./lanza-nginx.sh
curl -X POST http://127.0.0.1/api/amigos      -H "Content-Type: application/json"      -d '{"name": "Manolo", "lati": "43.5", "longi": "-5.6", "device": "Pixel 7"}'
exit
sudo poweroff
cd Sesion2_3
ls
cd amigos
ls
chmod +x *.sh
cd ..
chmod +x *.sh
ls
source ~/flaskenv/bin/activate
clear
docker build -t amigos:3.0
clear
docker build -t amigos:3.0
clear
docker build -t amigos:3.0
docker build -t amigos:3.0 .
ls
cd amigos/
ls
clear
docker build -t amigos:3.0 .
docker stop nginx amigos basedatos 2>/dev/null
cd ..
clear
docker stop nginx amigos basedatos 2>/dev/null
./lanza-basedatos.sh
./lanza-flask3.sh
./lanza-nginx.sh
curl -i http://127.0.0.1/health
docker ps -a --format "table {{.Names}}\t{{.Status}}"
docker logs amigos
docker logs nginx
clear
sudo poweroff
sudo chown -R uo287992:uo287992
cd Sesion2_3
cd amigos/
sudo chown -R uo287992:uo287992 sitios_nginx
ls
cd ..
ls
clear
sudo chown -R uo287992:uo287992 sitios_nginx
sudo chmod -R 755 sitios_nginx
docker stop nginx 2>/dev/null
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
docker stop nginx 2>/dev/null
./lanza-nginx.sh
curl -i http://127.0.0.1/health
docker ps -a --format "table {{.Names}}\t{{.Status}}"
docker logs nginx
clear
./lanza-nginx.sh
logs nginx
docker logs nginx
clear
./lanza-nginx.sh
curl -i http://127.0.0.1/health
docker rm -f nginx
clear
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
docker rm -f nginx amigos basedatos 2>/dev/null
./lanza-basedatos.sh
./lanza-flask3.sh
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
docker stop nginx 2>/dev/null
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
echo -e "\n=== DEFAULT.CONF ==="
cat sitios_nginx/default.conf
echo -e "\n=== LANZA NGINX ==="
cat lanza-nginx.sh
echo -e "\n=== CONTENEDORES ACTIVOS ==="
docker ps
echo -e "\n=== LOG DE ERROR DE NGINX ==="
docker run -d --name nginx_debug --network pruebas -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 nginx 2>/dev/null
sleep 2
docker logs nginx_debug
docker rm -f nginx_debug 2>/dev/null
clear
echo 'server {
    listen 80;
    server_name localhost;

    location / {
        resolver 127.0.0.11;
        proxy_pass http://amigos:5000;
    }
}' > sitios_nginx/default.conf
docker rm -f nginx 2>/dev/null
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
echo 'server {
    listen 80;
    server_name localhost;

    location / {
        resolver 127.0.0.11;
        proxy_pass http://amigos:5000;
    }
}' > sitios_nginx/default.conf
docker rm -f nginx 2>/dev/null
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
docker build -t amigos:3.0 .
cd amigos/
clear
ls
clear
docker build -t amigos:3.0 .
docker rm -f amigos
./lanza-flask3.sh
cd ..
docker rm -f amigos
./lanza-flask3.sh
curl -i http://127.0.0.1/health
clear
cd amigos/
docker build -t amigos:3.0 .
docker rm -f amigos
cd ..
./lanza-flask3.sh
curl -i http://127.0.0.1/health
# 1. Limpieza total y forzada
docker rm -f nginx amigos basedatos 2>/dev/null
# 2. Re-escribimos default.conf con el texto exacto, limpiando cualquier basura
mkdir -p sitios_nginx
cat << 'EOF' > sitios_nginx/default.conf
server {
    listen 80;
    server_name localhost;

    location / {
        resolver 127.0.0.11;
        proxy_pass http://amigos:5000;
    }
}
EOF

# 3. Lanzamos los tres contenedores en orden (asegurándonos de usar --rm en el script de nginx si no lo tenía)
./lanza-basedatos.sh
./lanza-flask3.sh
docker run -d --rm --network pruebas --name nginx -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 nginx
# 4. Le damos 2 segundos a Nginx para asentarse
sleep 2
# 5. Probamos el endpoint
curl -i http://127.0.0.1/health
clear
# 1. Limpieza total y forzada
docker rm -f nginx amigos basedatos 2>/dev/null
# 2. Corregir el Dockerfile para que Gunicorn arranque con la factoría correcta (create_app)
cat << 'EOF' > Dockerfile
FROM python:3.7
RUN pip install flask gunicorn flask-sqlalchemy pymysql flask-migrate prometheus-client
RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "lanzar:create_app('development')"]
EOF

# 3. Reconstruir la imagen de Flask para asentar los cambios
docker build -t amigos:3.0 .
# 4. Re-escribir default.conf con el texto exacto
mkdir -p sitios_nginx
cat << 'EOF' > sitios_nginx/default.conf
server {
    listen 80;
    server_name localhost;

    location / {
        resolver 127.0.0.11;
        proxy_pass http://amigos:5000;
    }
}
EOF

# 5. Lanzar los contenedores en orden
./lanza-basedatos.sh
./lanza-flask3.sh
docker run -d --rm --network pruebas --name nginx -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 nginx
# 6. Dar tiempo a que los servicios se asienten y probar
sleep 3
curl -i http://127.0.0.1/health
clear
# 1. Crear .dockerignore para que Docker no intente leer las carpetas problemáticas
echo "basedatos" > .dockerignore
echo "sitios_nginx" >> .dockerignore
# 2. Limpieza total y forzada
docker rm -f nginx amigos basedatos 2>/dev/null
# 3. Corregir el Dockerfile para que Gunicorn arranque con la factoría
cat << 'EOF' > Dockerfile
FROM python:3.7
RUN pip install flask gunicorn flask-sqlalchemy pymysql flask-migrate prometheus-client
RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "lanzar:create_app('development')"]
EOF

# 4. Reconstruir la imagen de Flask (ahora NO dará error de permisos)
docker build -t amigos:3.0 .
# 5. Re-escribir default.conf con el texto exacto
mkdir -p sitios_nginx
cat << 'EOF' > sitios_nginx/default.conf
server {
    listen 80;
    server_name localhost;

    location / {
        resolver 127.0.0.11;
        proxy_pass http://amigos:5000;
    }
}
EOF

# 6. Lanzar los contenedores en orden
./lanza-basedatos.sh
./lanza-flask3.sh
docker run -d --rm --network pruebas --name nginx -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 nginx
# 7. Dar tiempo a que los servicios se asienten y probar
sleep 3
curl -i http://127.0.0.1/health
clear
# 1. Limpieza
docker rm -f nginx amigos basedatos 2>/dev/null
# 2. Dejamos el Dockerfile con el comando original lanzar:app que usabas en la sesión 2.2
cat << 'EOF' > Dockerfile
FROM python:3.7
RUN pip install flask gunicorn flask-sqlalchemy pymysql flask-migrate prometheus-client
RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "lanzar:app"]
EOF

# 3. Construimos rapidísimo porque ya está en caché
docker build -t amigos:3.0 .
# 4. Lanzamos todo en orden
./lanza-basedatos.sh
./lanza-flask3.sh
docker run -d --rm --network pruebas --name nginx -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 nginx
# 5. Esperamos 3 segundos y probamos
sleep 3
curl -i http://127.0.0.1/health
clear
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
docker rm -f nginx amigos 2>/dev/null
# Lanzamos amigos sin que se auto-destruya
docker run -d --name amigos --network pruebas amigos:3.0
sleep 2
echo -e "\n=== LOGS DE AMIGOS ==="
docker logs amigos
# Lanzamos nginx sin que se auto-destruya
docker run -d --name nginx -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 --network pruebas nginx
sleep 2
echo -e "\n=== LOGS DE NGINX ==="
docker logs nginx
clear
# 1. Limpieza
docker rm -f nginx amigos basedatos 2>/dev/null
# 2. Creamos el Dockerfile EN LA CARPETA CORRECTA (amigos/)
cat << 'EOF' > amigos/Dockerfile
FROM python:3.7
RUN pip install flask gunicorn flask-sqlalchemy pymysql flask-migrate prometheus-client
RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "lanzar:app"]
EOF

# 3. Entramos a la carpeta de código, construimos la imagen y salimos
cd amigos
docker build -t amigos:3.0 .
cd ..
# 4. Lanzamos la arquitectura en orden
./lanza-basedatos.sh
./lanza-flask3.sh
docker run -d --rm --network pruebas --name nginx -v $(pwd)/sitios_nginx:/etc/nginx/conf.d -p 80:80 nginx
# 5. Probamos por fin el endpoint
sleep 3
curl -i http://127.0.0.1/health
clear
ls
docker rm -f nginx amigos basedatos 2>/dev/null
./lanza-basedatos.sh
./lanza-flask3.sh
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
docker logs --tail 30 nginx
docker logs --tail 30 amigos
docker images | grep amigos
cat lanza-flask3.sh
sudo ss -tlnp | grep ':80'
curl -i http://127.0.0.1:5000/health
clear
cat lanza-nginx.sh 
cd amigos
cat Dockerfile 
cd ..
clear
docker run --name amigos   -e DEPLOYMENT_MODE=production   -e DATABASE_URI="mysql+pymysql://amigosuser:amigospass@basedatos/amigosdb"   --network pruebas amigos:3.0
docker rm -f amigos
clear
ls -R app | grep -v pyc
cat app/__init__.py
clear
cd amigos
docker build -t amigos:3.0 .
cd ..
docker rm -f nginx amigos basedatos 2>/dev/null
./lanza-basedatos.sh
./lanza-flask3.sh
./lanza-nginx.sh
curl -i http://127.0.0.1/health
clear
cd amigos/
docker build -t amigos:3.0 .
cd ..
docker rm -f amigos
./lanza-flask3.sh
curl -i http://127.0.0.1/metrics
chmod +x lanza-prometheus.sh
clear
# Si apagaste algún contenedor antes, los levantamos todos:
./lanza-basedatos.sh
./lanza-flask3.sh
./lanza-nginx.sh
# Y ahora lanzamos al nuevo invitado:
./lanza-prometheus.sh
clear
docker ps | grep prometheus
docker logs prometheus
curl -I http://127.0.0.1:9090
clear
docker run --rm --name prometheus_debug --network pruebas -p 9090:9090 -v $(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
./lanza-prometheus.sh
clear
for i in {1..100}; do   curl -s http://127.0.0.1/health > /dev/null;   curl -s http://127.0.0.1/html/amigos > /dev/null;   curl -s http://127.0.0.1/ruta-falsa > /dev/null; done
cd ..
clear
git commit --allow-empty -m "Terminada Sesión 2.3: Servidor Prometheus desplegado y pruebas de tráfico visualizadas"
git push
cd Sesion3
clear
sudo apt-get install telnetd
sudo nano /etc/inetd.conf
sudo systemctl restart inetd
source ~/flaskenv/bin/activate
clear
sudo systemctl status inetd
exit
cd Sesion3
clear
sudo systemctl status inetd
sudo apt-get install telnetd
/etc/inetd.conf
clear
source ~/flaskenv/bin/activate
sudo apt-get install telnetd
sudo nano /etc/inetd.conf
sudo systemctl restart inetd
python3 telnet1_ejemplo.py
python3 telnet1_ejemplo_mejorado.py
python3 telnet2_lanza_servidor.py
exit
ifconfig
hostname -I
ifconfig
clear
ifconfif
ifconfig
sudo poweroff
clear
ifconfig
ls /etc/netplan
sudo nano /etc/netplan/50-cloud-init.yaml 
clear
sudo netplan try
ls /home
exit
ps -ef
nohup python3 udp_servidor3_con_ok.py &
exit
