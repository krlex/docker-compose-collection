Matomo
=====

Matomo, formerly Piwik, is a free and open source web analytics application developed by
a team of international developers, that runs on a PHP/MySQL webserver. It tracks online
visits to one or more websites and displays reports on these visits for analysis.

## docker-compose.yml

```
x-matomo-environment: &matomo_environment
  - MATOMO_DATABASE_HOST=mysql
  - MATOMO_DATABASE_ADAPTER=mysql
  - MATOMO_DATABASE_TABLES_PREFIX=matomo_
  - MATOMO_DATABASE_USERNAME=matomo
  - MATOMO_DATABASE_PASSWORD=matomo
  - MATOMO_DATABASE_DBNAME=matomo

x-mysql-environment: &mysql_environment
  - MYSQL_PASSWORD=matomo
  - MYSQL_DATABASE=matomo
  - MYSQL_USER=matomo

services:

  mysql:
    image: mysql
    volumes:
      - ./data/mysql:/var/lib/mysql
    environment: *mysql_environment
    restart: unless-stopped

  matomo:
    image: matomo
    ports:
      - "8000:80"
    environment: *matomo_environment
    restart: unless-stopped
```

## Vagrant

In case you have problem with docker and docker-compose. You can use vargantfile

```
vagrant up
```
