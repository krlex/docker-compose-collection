AWX
===

# About AWX

AWX provides a web-based user interface, REST API, and task
engine built on top of Ansible. It is the upstream project
for Tower, a commercial derivative of AWX.

## Tree

```
data
├── projects
│   └── example
│       └── playbook.yml
├── redis
│   ├── redis_socket (mode:777)
│   └── redis.conf
└── settings
    ├── SECRET_KEY
    ├── credentials.py
    ├── environment.sh
    └── nginx.conf
```

## Running

```bash
$ mkdir -m 777 -p data/redis/redis_socket
$ docker-compose up -d
$ docker-compose exec web bash
>>> awx-manage inventory_import --inventory-name=xxx --source=/path/to/inventory.ini
INFO     Reading Ansible inventory source: /path/to/inventory.ini
INFO     Loaded 1 groups, 30 hosts
INFO     Inventory import completed for  (xxx - 13) in 1.0s
>>> chown -R nginx:nginx /var/lib/nginx # XXX: https://github.com/ansible/awx/issues/5230
>>> exit
$ curl http://admin:password@127.0.0.1:8052
```

## Vagrant

if you have problem with docker, you can use vagrant

```
vagrant up
```
