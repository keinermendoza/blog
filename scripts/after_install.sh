#!/usr/bin/env bash

# get direction before install
sudo pwd > aqui.txt
sudo mv aqui.txt /home/

# go into the blog floder
cd ./blog

# Create images using the docker-compose
sudo docker compose build

# Start the containers
sudo docker compose up --detach
