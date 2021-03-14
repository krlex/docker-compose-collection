Certbot
=======

Certbot is a free, open source software tool for automatically using
Let's Encrypt certificates on manually-administrated websites to enable HTTPS.
Certbot is made by the Electronic Frontier Foundation (EFF), a 501(c)3
nonprofit based in San Francisco, CA, that defends digital privacy,
free speech, and innovation.

## docker-compose.yml

```
certbot:
  image: quay.io/letsencrypt/letsencrypt
  command: certonly --standalone
  ports:
    - "80:80"
    - "443:443"
  volumes:
    - /etc/letsencrypt:/etc/letsencrypt
    - /var/lib/letsencrypt:/var/lib/letsencrypt
```

## up and running

```
# stop nginx (release 80/tcp and 443/tcp)
$ systemctl stop nginx

# generate keys (interactive)
$ docker-compose run --rm --service-ports certbot
>>> email: admin@example.com
>>> domains: example.com,blog.example.com,wiki.example.com

# renew keys (headless)
$ crontab -l
0 0 * * * cd ~/fig/certbot && docker-compose run --rm certbot renew >> renew.log

# list keys
$ tree /etc/letsencrypt/live/
/etc/letsencrypt/live/
└── example.com
    ├── cert.pem -> ../../archive/example.com/cert1.pem
    ├── chain.pem -> ../../archive/example.com/chain1.pem
    ├── fullchain.pem -> ../../archive/example.com/fullchain1.pem
    └── privkey.pem -> ../../archive/example.com/privkey1.pem

# deploy keys
$ mkdir -p /etc/nginx/ssl/
$ cp /etc/letsencrypt/live/example.com/fullchain.pem /etc/nginx/ssl/example.com.crt
$ cp /etc/letsencrypt/live/example.com/privkey.pem /etc/nginx/ssl/example.com.key

# reconfig nginx
$ vi /etc/nginx/sites-enabled/default
server {
    listen 80 default;
    server_name _;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com blog.example.com;
    ssl_certificate ssl/example.com.crt;
    ssl_certificate_key ssl/example.com.key;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

# start nginx
$ systemctl start nginx
```

You can also generate keys without docker.

```bash
# install
apt install build-essential dialog libffi-dev libssl-dev python3-dev python3-pip
pip3 install letsencrypt

# generate
letsencrypt certonly --standalone -d example.com -d blog.example.com -d wiki.example.com

# deploy
mkdir -p /etc/nginx/ssl
cp /etc/letsencrypt/live/example.com/fullchain.pem /etc/nginx/ssl/example.com.crt
cp /etc/letsencrypt/live/example.com/privkey.pem /etc/nginx/ssl/example.com.key

# renew
letsencrypt renew
```

## Vagrant

If you have problem with docker and docker-compose. Than you can use this vagrantfile

```
vagrant up
```
