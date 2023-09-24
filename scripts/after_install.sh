#!/usr/bin/env bash

# go into the blog floder
cd /home/ubuntu/blog/

# Create images using the docker-compose
sudo docker compose build

# Start the containers
sudo docker compose up --detach
