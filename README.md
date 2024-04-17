# FastAPI_project
Для того чтобы запустить проект потребуется docker

Для установки docker воспользуйтесь [инструкцией](https://losst.pro/ustanovka-docker-na-ubuntu-16-04)

Ниже следующие команды выполнять в терминале

Для сборки docker контейнера: 

``
sudo docker build -t fastapi .
``

Для запуска сервера введите команду:

``
sudo docker run --rm -p 80:80 fastapi
``

Переходим по [ссылке](http://0.0.0.0:80)


