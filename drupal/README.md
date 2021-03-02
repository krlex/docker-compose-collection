Drupal
======

# About Drupal

Drupal is a free and open-source web content management framework written in PHP and distributed under the GNU General Public License. Drupal provides a back-end framework for at least 12% of the top 10,000 websites worldwide – ranging from personal blogs to corporate, political, and government sites


```
drupal:
  image: drupal
  ports:
    - "8080:80"
  links:
    - mysql
    ```
  restart: always
```
cd ~/vagrant/drupal/
docker-compose up -d drupal


http://127.0.0.1:8080
```

# Vagrant

This installation is setup for Vagrant also if you can install docker on your host (for example FreeBSD). But you can install `vagrant`

```
vagrant up
```
