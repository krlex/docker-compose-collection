Consul
======

# About Consul

Consul is a software first released in 2014 for DNS-based service discovery
and provides distributed Key-value storage, segmentation and configuration.
Registered services and nodes can be queried using a DNS interface or an
HTTP interface.

## in docker-compose
```
consul:
image: progrium/consul
restart: always
hostname: consul
ports:
  - 8500:8500
command: "-server -bootstrap"
```

# Vagrant

If you have problem with docker or docker compose use vagrant.

```
vagrant up
```
