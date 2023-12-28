#!/bin/bash

# Clone the repository
git clone https://github.com/Inframous/HomeApi.git
cd HomeApi || exit

# Build the Docker image
sudo docker build -t "homeapi" .

# Launch the container
sudo docker run -d -p 8080:5000 --restart always --name homeapi homeapi
