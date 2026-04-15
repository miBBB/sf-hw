docker build . -t ifav \n
docker run -d --name myifav -e SITE_URL="https://ya.ru/" -v /tmp/ifav:/opt/favicons/img ifav \n
ls /tmp/ifav/ \n
docker rm myifav \n 
