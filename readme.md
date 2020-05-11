docker-compose.yml
    build: это то место где находится dockerfile

разница между локалхост и 0,0,0,0
    https://superuser.com/questions/949428/whats-the-difference-between-127-0-0-1-and-0-0-0-0 

запущенные контейнеры
    docker ps
попасть внутрь контейнера
    docker exec -it <mycontainer_id_or_name> bash

все контейнеры которые есть
    docker container ls -a

запустить контейнер
    docker-compose up
    docker-compose up --build (билд и запуск)
    docker-compose build (просто билд, выполнить dockerfile)
    

удалить контейнер
    docker container rm <mycontainer_id_or_name>
    https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/