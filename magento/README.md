Magento
=======

# About Magento

Magento is an ecommerce platform built on open source technology which provides online
merchants with a flexible shopping cart system, as well as control over the look,
content and functionality of their online store.


## Docker-compose.yml

```yaml
magento:
  image: vimagick/magento
  ports:
    - "8000:80"
  links:
    - mysql
  restart: always

mysql:
  image: mysql
  environment:
    - MYSQL_ROOT_PASSWORD=root
    - MYSQL_DATABASE=magento
  restart: always
```

# with Vagrant

If you have problem with installation docker on your host. You can use this Vagrantfile.

```
vagrant up
```

