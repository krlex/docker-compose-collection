Odoo
====

# About Odoo

Odoo is a suite of business management software tools including CRM, e-commerce,
billing, accounting, manufacturing, warehouse, project management, and inventory
management to name a few. The Community version is a libre software, licensed
under the GNU LGPLv3.

## In Docker-compose.yml

```yaml
odoo:
  image: odoo:12
  ports:
    - "127.0.0.1:8069:8069"
  volumes:
    - ./data/config:/etc/odoo
    - ./data/web:/var/lib/odoo
    - ./data/addons:/mnt/extra-addons
  links:
    - postgres:db
  restart: always

postgres:
  image: postgres:11-alpine
  volumes:
    - ./data/postgres:/var/lib/postgresql/data
  environment:
    - POSTGRES_USER=odoo
    - POSTGRES_DB=postgres
    - POSTGRES_PASSWORD=odoo
  restart: always
```

## Manual starting

```bash
$ mkdir -m 777 -p data/web
$ docker-compose up -d
$ curl http://localhost:8069
```

## Vagrant

```
vagrant up
```
