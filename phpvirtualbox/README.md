phpVirtualBox
=============

This is a fork of [jazzdd86/phpvirtualbox](https://hub.docker.com/r/jazzdd/phpvirtualbox/).

[phpVirtualBox][1] is a web-based front-end to VirtualBox written in PHP.

### docker-compose.yml

```yaml
phpvirtualbox:
  image: vimagick/phpvirtualbox
  ports:
    - "8888:80"
  environment:
    - ID_PORT_18083_TCP=remote-server:18083
    - ID_NAME=Vbox
    - ID_USER=username
    - ID_PW=password
    - CONF_browserRestrictFolders=/data,
  restart: always
```

> - Make sure you can login `remote-server` with `username:password`.
> - ISO images can be placed at `/data` directory on `remote-server`.
> - During the OS installation, you can connect to it with RDP viewer.

### vboxweb.service

```
# /etc/systemd/system/vboxweb.service
[Unit]
Description=VirtualBox Web Service
After=network.target

[Service]
ExecStart=/usr/bin/vboxwebsrv -H 0.0.0.0 -p 18083
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### server setup

```bash
# install virtualbox
echo "deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" > /etc/apt/sources.list.d/virtualbox.list
wget -O- http://download.virtualbox.org/virtualbox/debian/oracle_vbox_2016.asc | apt-key add -
apt-get update
apt-get install -y virtualbox-5.1 dkms
systemctl status vboxdrv

# install extpack
wget https://download.virtualbox.org/virtualbox/6.1.18/Oracle_VM_VirtualBox_Extension_Pack-6.1.18.vbox-extpack
VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-6.1.18.vbox-extpack
VBoxManage list extpacks

# install vagrant
wget https://releases.hashicorp.com/vagrant/2.2.14/vagrant_2.2.14_x86_64.deb
dpkg -i vagrant_2.2.14_x86_64.deb
vagrant version

# start vm
vagrant box add debian/jessie64
vagrant init debian/jessie64
vagrant up

# disable vboxweb-service
systemctl stop vboxweb-service
systemctl disable vboxweb-service

# enable vboxweb
systemctl daemon-reload
systemctl start vboxweb
systemctl enable vboxweb
```
