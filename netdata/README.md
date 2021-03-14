Netdata
=======

Netdata is an open source tool designed to collect real-time metrics,
such as CPU usage, disk activity, bandwidth usage, website visits, etc.,
and then display them in live, easy-to-interpret charts.
The tool is designed to visualize activity in the greatest possible detail,
allowing the user to obtain an overview of what is happening and what has
just happened in their system or application.

## docker-compose

```
netdata:
  image: netdata/netdata
  hostname: example.com
  ports:
    - 19999:19999
  cap_add:
    - SYS_PTRACE
  security_opt:
    - apparmor:unconfined
  volumes:
    - /proc:/host/proc:ro
    - /sys:/host/sys:ro
    - /var/run/docker.sock:/var/run/docker.sock:ro
  restart: always
```

## vagrant

If you have problem with installation docker and docker-compose. You can use vagrant.

```
vagrant up
```
