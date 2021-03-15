Rundeck
=======

# About Rundeck

the Rundeck software platform to enable operations run more efficiently
and scale faster while maintaining security and compliance.

## docker-compose.yml

```
rundeck:
  image: rundeck/rundeck:3.0.22
  ports:
    - "4440:4440"
  volumes:
    - ./data/ssh:/home/rundeck/.ssh
    - ./data/rundeck:/home/rundeck/server/data
  environment:
    - RUNDECK_SECURITY_HTTPHEADERS_ENABLED=false
  mem_limit: 1024m
  restart: always
```

Read [this][2] to use more environment variables.

## up and running

```
$ mkdir -p data/{rundeck,ssh,postgres}
$ chown -R 1000:1000 data
$ chmod 700 data/ssh
$ docker-compose up -d
$ curl http://127.0.0.1:4440
```
## Vagrant

If you have problem with docker and docker-compose. You can use vagrant

```
vagrant up
```
