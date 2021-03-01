gitea
=====

Gitea is an open-source forge software package for hosting software
development version control using Git as well as other collaborative
features like bug tracking, wikis and code review.

This is how i config gitea server

```
  server:
    image: gitea/gitea
    ports:
      - "2222:22"
      - "3000:3000"
    volumes:
      - ./data/gitea:/data
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - DB_TYPE=postgres
      - DB_HOST=postgres:5432
      - DB_NAME=gitea
      - DB_USER=gitea
      - DB_PASSWD=gitea
    depends_on:
      - postgres
    restart: always
```

and this is my "way" how to create simple postgresql

```
  postgres:
    image: postgres:12-alpine
    ports:
      - "5432:5432"
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=gitea
      - POSTGRES_PASSWORD=gitea
      - POSTGRES_DB=gitea
    restart: always
```

In my case i install all this in vagrant. I use FreeBSD and they dont use docker. So i create for myself Vagrantfile
which is gona help me to use docker and docker-compose

I just do:

```
vagrant up
```

