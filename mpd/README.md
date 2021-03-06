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

$ wget https://upload.wikimedia.org/wikipedia/commons/d/d5/Pop_Goes_the_Weasel.ogg -O data/music/test.ogg

# FIXME: OUTDATED
$ curl -s -X POST -H 'Content-Length: 0' http://www.shoutcast.com/Home/Top |
    jq '.[].ID' |
      parallel --eta -k curl -s 'http://yp.shoutcast.com/sbin/tunein-station.m3u?id={}' |
        sed '1!s@#EXTM3U@@' |
          cat -s > data/playlists/shoutcast.m3u

$ cat > data/playlists/microphone.m3u << _EOF_
#EXTM3U
#EXTINF:-1,microphone
alsa://plughw:1,0
_EOF_

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
