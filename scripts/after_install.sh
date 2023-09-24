#!/usr/bin/env bash

# go into the blog floder
cd home/ubuntu/blog

# get direction before install
sudo pwd > aqui.txt
sudo mv aqui.txt /home/

# Create images using the docker-compose
sudo docker compose build

# Start the containers
sudo docker compose up --detach
