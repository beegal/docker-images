FROM python:3.12.2-bookworm

RUN pip install --upgrade pip; pip install mpmath flask; mkdir /var/www; chown www-data:www-data /var/www
COPY service.py /var/www
USER www-data
ENTRYPOINT python3 /var/www/service.py
EXPOSE 6000


