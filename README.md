# yamdb_final
yamdb_final


![yamdb_final](https://github.com/Chinilshik-kalkulatorov/yamdb_final/actions/workflows/yamdb_workflow/badge.svg)

____
Сервис доступен по ссылке: [Yamdb](http://62.84.121.48/api/v1/)  
Документация по ссылке: [Redoc](http://62.84.121.48/redoc/)

Требования
Для запуска этого проекта необходимо установить следующие компоненты:

Docker
Docker Compose
Настройка
Склонируйте этот репозиторий на свой локальный компьютер.
```
$ git clone https://github.com/username/docker-compose-project.git
```
Перейдите в директорию проекта.
```
$ cd docker-compose-project
```
Отредактируйте файл docker-compose.yml, если это необходимо, и добавьте все необходимые контейнеры и сервисы.
Запуск
Запустите Docker Compose командой:
```
$ docker-compose up
```
Отслеживайте состояние запущенных контейнеров и сервисов:
```
$ docker-compose ps
```
Требования
----------
* Python 3.8+


Установка 
----------


1. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env

source env/bin/activate
```
2. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
3. Выполнить миграции:
```bash
cd api_yamdb

python3 manage.py migrate
```
4. Запустить проект:
```bash
python3 manage.py runserver
```

Файл фикстур:
```
$ python manage.py loaddata fixtures.json 
```
Переменные окружения:

Для корректной работы проекта требуется определить следующие переменные окружения:

DEBUG - включение режима отладки (True/False)
SECRET_KEY - секретный ключ Django проекта
DATABASE_URL - URL базы данных
Эти переменные можно определить в файле .env в корневой директории проекта.

Проект написал Билол Адхамов в здравом уме и без виски в руке