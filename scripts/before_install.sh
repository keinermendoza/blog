#!/usr/bin/env bash

# stop all the containers
sudo docker container stop $(sudo docker container ps -aq)

# remove all the containers
sudo docker container rm $(sudo docker container ps -aq)

# delete app
sudo rm -rf /home/ubuntu/blog


