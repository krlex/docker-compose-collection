Music Player Daemon
===================

# About MPD

Music Player Daemon (MPD) is a free and open music player server.
It plays audio files, organizes playlists and maintains a music
database. In order to interact with it, a client program is needed.
The MPD distribution includes mpc, a simple command line client.

MPD is used in proprietary audio hardware. The MPD project maintains a list of vendors, some of which infringe the GPL.


## docker-compose.yml

```yaml
version: "3.8"

services:

  mpd:
    image: vimagick/mpd
    ports:
      - "6600:6600"
      - "8800:8800"
    volumes:
      - ./data/config:/root/.config
      - ./data/music:/var/lib/mpd/music
      - ./data/playlists:/var/lib/mpd/playlists
    devices:
      - /dev/snd
    restart: unless-stopped
```

## Server Setup

```bash
$ mkdir -p ~/vagrant/mpd/{config,music,playlists}
$ cd ~/vagrant/mpd/

$ docker-compose up -d
$ docker-compose exec mpd sh
>>> mpc help
>>> mpc update
>>> mpc ls | mpc add
>>> mpc repeat on
>>> mpc random on
>>> mpc
>>> mpc clear
>>> mpc lsplaylists
>>> mpc load shoutcast
>>> mpc play
>>> exit
```
## Vagrant

If you have problem with docker installation. You can use this vagrantfile
start using docker inside the vagrant

```
vagrant up
```
