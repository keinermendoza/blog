#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /home/ubuntu/blog/

# activate virtual environment
python3 -m venv venv
source venv/bin/activate

# install requirements.txt
pip install -r /home/ubuntu/blog/requirements.txt

# puting staticfiles on a single static folder
python3 manage.py collectstatic

# ubicandome en la base
cd

# iniciando gunicorn modo daemon
gunicorn -c conf/gunicorn_config.py blog.mysite.wsgi -D

# iniciando nginx
sudo service ngnix start

# copy my custom config of ngnix on it's default folder
sudo cp --f home/ubuntu/blog/sites-available /etc/nginx/sites-available

# entry to nginx folder
cd /etc/nginx/sites-enabled

# linkig to my project
sudo ln -s /etc/nginx/sites-available/blog

# restarting ngnix
sudo systemctl restart ngnix

# migrate database sqlite for test
python3 manage.py migrate

# run server
screen -d -m python3 manage.py runserver 0:8000
