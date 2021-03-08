Yourls
======

# About Yourls
Yourls is a small set of PHP scripts that will allow you to run
your own URL shortening service (a la TinyURL). You can make it
private or public, you can pick custom keyword URLs, it comes
with its own API. You will love it.

## inside docker-compose.yml

```yaml
version: '3.8'

services:

  yourls:
    image: yourls:1.7
    ports:
      - "8080:80"
    environment:
      - YOURLS_DB_HOST=mysql
      - YOURLS_DB_USER=root
      - YOURLS_DB_PASS=root
      - YOURLS_DB_NAME=yourls
      - YOURLS_USER=admin
      - YOURLS_PASS=admin
      - YOURLS_SITE=https://yourls.example.com
    depends_on:
      - mysql
    restart: unless-stopped

  mysql:
    image: mysql:5.7
    volumes:
      - ./data:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=yourls
    restart: unless-stopped
```

## This is how to  Up and Running

```bash
$ docker-compose up -d
$ docker cp yourls_yourls_1:/var/www/html/user/config.php .
$ vi config.php
$ chown www-data:www-data config.php
$ chmod 664 config.php
$ docker cp config.php yourls_yourls_1:/var/www/html/user/
```
## or you can run this file (files in files/config.php)

```bash
$ docker cp files/config.php yourls_yourls_1:/var/www/html/user
```

## File: config.php

```php
/** Username(s) and password(s) allowed to access the site. Passwords either in plain text or as encrypted hashes
 ** YOURLS will auto encrypt plain text passwords in this file
 ** Read http://yourls.org/userpassword for more information */
$yourls_user_passwords = [
    'user1' => 'secret1',
    'user2' => 'secret2',
];
```

## How to Backup and Restore

# backup

```
$ docker-compose exec -T mysql mysqldump -uroot -proot yourls > yourls-$(date +%F).sql
```
# restore

```
$ docker exec -i yourls_mysql_1 mysql -uroot -proot yourls < yourls-$(date +%F -d yesterday).sql
```
