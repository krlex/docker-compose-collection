jenkins
=======

## what is in  docker-compose.yml

```yaml
jenkins:
  image: jenkins/jenkins:lts-alpine
  ports:
    - "8080:8080"
    - "5000:5000"
  volumes:
    - ./data:/var/jenkins_home
  environment:
    - JAVA_OPTS=-Dhudson.footerURL=http://jenkins.easypi.pro
  restart: always
```

## up and running

```bash
$ cd ~/repo/jenkins
$ mkdir -p data
$ sudo chown 1000 data
$ docker-compose up -d
$ docker-compose exec jenkins bash
>>> cat ~/secrets/initialAdminPassword
******
>>> ssh-keygen
>>> cat ~/.ssh/id_rsa.pub
......
>>> exit
$ docker-compose exec --user root jenkins apk add -U git
$ http://localhost:8080/
```

## if you want fix slow network

```
$ vim data/war/jsbundles/pluginSetupWizard.js
    // default 10 seconds for AJAX responses to return before triggering an error condition
    var pluginManagerErrorTimeoutMillis = 10 * 1000;
```

## Why Vagrant?

If you dont use Linux (in my case i use FreeBSD). I create Vagrantfile with installation and starting up docker-compose with his provision.

## Warning

If you want to see your first password remove `-d`
for example:

```
docker-compose up -d
```
this should looks like:

```
docker-compose up
```

You can also do this in Vagrantfile
but if you break with `CTRL + C` it wil stop working.
My recommendation is do not remove `-d` if you know what are you doing


