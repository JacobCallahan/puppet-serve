FROM httpd

RUN echo "deb http://ftp.de.debian.org/debian testing main" > /etc/apt/sources.list
RUN echo 'APT::Default-Release "stable";' | tee -a /etc/apt/apt.conf.d/00local
RUN apt-get update && apt-get -y -t testing install python3.6

COPY / /
RUN cd / && python3 /prepare_repo.py
RUN cp -r /serve/* /usr/local/apache2/htdocs/ && rm /usr/local/apache2/htdocs/index.html

CMD httpd-foreground