FROM debian:latest

RUN apt update
RUN apt install -y curl wget unzip git apache2 libapache2-mod-php mariadb-server \
        mariadb-client php mcrypt php-mbstring php-mysql php-gd php-curl

RUN service apache2 start
RUN service mysql start

RUN wget http://open-real-estate.info/files/OpenRealEstateV1.34.0_en.zip
RUN mkdir /var/www/html/openrealestate
RUN unzip OpenRealEstateV1.34.0_en.zip -d /var/www/openrealestate
RUN chown -R www-data:www-data /var/www/html/openrealestate

RUN git clone https://github.com/krlex/DataBase-scripts && cd DataBase-scripts/
RUN bash DataBase-scripts/create-mariadb-ansible.sh openrealestatedb user password
RUN echo "\
<VirtualHost *:80> \
        ServerAdmin admin@example.com \
        DocumentRoot /var/www/html/openrealestate/ \
        ServerName www.example.com \
<Directory /var/www/html/openrealestate/> \
        Options FollowSymLinks \
        AllowOverride All \
        Order allow,deny \
        allow from all \
</Directory> \
        ErrorLog /var/log/apache2/openrealestate-error_log \
        CustomLog /var/log/apache2/openrealestate-access_log common \
</VirtualHost>" \
> /etc/apache2/sites-available/openrealestate.conf

RUN a2enmod rewrite
RUN a2ensite openrealestate
RUN service apache2 restart
