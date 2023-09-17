#!/usr/bin/env bash

# sudo systemctl stop nginx
# sudo apt-get remove nginx

# clean codedeploy-agent files for a fresh install
sudo rm -rf /home/ubuntu/install

# stop and uninstall nginx
sudo nginx -s stop
sudo apt-get remove --purge nginx* -y

# install CodeDeploy agent
sudo apt-get -y update
sudo apt-get -y install ruby
sudo apt-get -y install wget
cd /home/ubuntu
wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
sudo chmod +x ./install 
sudo ./install auto

# update os & install python3 and libpq-dev for postgresql
sudo apt-get update
sudo apt-get install -y python3 python3-dev python3-pip python3-venv libpq-dev
pip install --user --upgrade virtualenv

# delete app
sudo rm -rf /home/ubuntu/blog


