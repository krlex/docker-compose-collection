OWNCloud
========

# About OwnCloud

ownCloud is a file server that enables secure storage, collaboration and
sharing. It is convenient to store files in the cloud, so they are
available on any device and can be shared with a few clicks.

## docker-compose.yml

```
owncloud:
  image: owncloud
  ports:
    - "8080:80"
  volumes:
    - ./data:/var/www/html/data
  restart: always

```

## Vagrant

If you have problem with installation  docker and docker-compose

you can use vagrant and it will work fine
