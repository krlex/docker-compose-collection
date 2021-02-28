# Jira
======

# About Jira
Jira Software is part of a family of products designed to help teams of all types manage work.
Originally, Jira was designed as a bug and issue tracker. But today, Jira has evolved into a
powerful work management tool for all kinds of use cases, from requirements and test case management
to agile software development.

# Manual

```bash
$ mkdir -p data/jira
$ chown 1000:1000 data/jira
$ docker-compose up -d
$ docker-compose exec postgres psql -U jira
>>> select * from propertystring where id in (select id from propertyentry where PROPERTY_KEY='jira.sid.key');
  id   |    propertyvalue
-------+---------------------
 10101 | BP8Q-WXN6-SKX3-NB5M
>>> \q
$ curl http://localhost:8080/
```
# Vagrant

Just start with:

```
vagrant up
```

