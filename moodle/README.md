moodle
======

# About Moodle

Moodle is a learning platform designed to provide educators,
administrators and learners with a single robust, secure and
integrated system to create personalised learning environments.
You can download the software onto your own web server or ask
one of our knowledgeable Moodle Partners to assist you.


## docker-compose.yml

```
moodle:
  image: vimagick/moodle
  ports:
    - "8000:80"
  links:
    - mysql
  volumes:
    - ./moodledata:/var/www/moodledata
  restart: always

mysql:
  image: mysql
  environment:
    - MYSQL_ROOT_PASSWORD=root
    - MYSQL_DATABASE=moodle
  restart: always
```

## up and running

```
$ cd ~/moodle/
$ mkdir -p moodledata
$ chmod 777 moodledata
$ docker-compose up -d
```
and go to:
http://localhost:8000

# vagrant

```
vagrant up
```
