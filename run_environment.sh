#!/bin/bash

#docker run --name dbcontainer -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -d percona:latest &&
#docker run --name vkmock -p 8083:8083 -d vk_api:latest &&
docker start dbcontainer && docker start vkmock &&
docker run -v "/home/rus/Рабочий стол/:/home" -p 81:81 --link dbcontainer:dbhost --link vkmock:vkhostname myapp /app/myapp --config="/home/conf" --setup
