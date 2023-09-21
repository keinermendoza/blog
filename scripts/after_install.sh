# #!/usr/bin/env bash

# # kill any servers that may be running in the background 
# sudo pkill -f runserver

# # kill frontend servers if you are deploying any frontend
# # sudo pkill -f tailwind
# # sudo pkill -f node

# # este no cd /home/ubuntu/blog/

# # activate virtual environment
# python3 -m venv venv
# source venv/bin/activate

# # install requirements.txt
# pip install -r /home/ubuntu/blog/requirements.txt

# copy my custom gunicorn conf folder to the root
# sudo cp -r blog/conf /home/ubuntu

# # puting staticfiles on a single static folder
# # # revision python3 manage.py collectstatic

# # ubicandome en la base
# # #cd

# # instalando nginx
# sudo apt install nginx -y

# # iniciando gunicorn modo daemon
# gunicorn -c conf/gunicorn_config.py mysite.wsgi -D

# # iniciando nginx
# sudo service ngnix start


# # copy my custom conf sites-available
# sudo cp home/ubuntu/blog/sites-available/blog /etc/nginx/sites-available

# # entry to nginx folder
# cd /etc/nginx/sites-enabled/

# # linkig to my project
# sudo ln -s /etc/nginx/sites-available/blog

# # restarting ngnix
# sudo systemctl restart nginx

# # migrate database sqlite for test
# python3 manage.py migrate

# # run server
# screen -d -m python3 manage.py runserver 0:8000
