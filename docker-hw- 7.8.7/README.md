docker build . -t ifav 
docker run -d --name myifav -e SITE_URL="https://ya.ru/" -v /tmp/ifav:/opt/favicons/img ifav 
ls /tmp/ifav/
docker rm myifav 
