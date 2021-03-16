nextcloud
=========

## docker-compose.yml

```yaml
nextcloud:
  image: indiehosters/nextcloud
  ports:
    - "127.0.0.1:9000:9000"
  volumes:
    - ./data/apps:/var/www/html/apps
    - ./data/config:/var/www/html/config
    - ./data/data:/var/www/html/data
  restart: always

nginx:
  image: nginx:alpine
  volumes:
    - ./nginx.conf:/etc/nginx/conf.d/default.conf
    - ./ssl:/etc/nginx/ssl
  volumes_from:
    - nextcloud
  net: host
  restart: always
```

## Server Setup

```bash
$ docker-compose up -d

$ docker-compose exec -u www-data nextcloud ./occ files:scan --all
Starting scan for user 1 out of 1 (admin)
+---------+-------+--------------+
| Folders | Files | Elapsed time |
+---------+-------+--------------+
| 10      | 21    | 00:00:00     |
+---------+-------+--------------+

$ crontab -l
0 * * * * docker exec -u www-data nextcloud_nextcloud_1 ./occ files:scan --all
```
