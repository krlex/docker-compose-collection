Rocket.Chat
===========

# About Rocket Chat
Today, Rocket. Chat is an open source communication hub that enables
banks, NGOs, startups, and governmental organizations to have their
own chat tool, customize its look and feel, choose their users, and
securely manage data.


## up and running

```
$ docker-compose up -d mongo
$ docker-compose exec mongo mongo
>>> rs.initiate({_id: 'rs0', members: [{_id: 0, host: 'localhost:27017'}]})
>>> exit
$ docker-compose up -d rocketchat
$ curl http://127.0.0.1:3000
```
## Vagrant

If you have problem with docker and docker-compose installation. You can use
vagrant

```
vagrant up
```
