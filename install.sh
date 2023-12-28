#!/bin/bash

PORT=6500 

# Clone the repository
git clone https://github.com/Inframous/HomeApi.git
cd HomeApi || exit

# Build the Docker image
sudo docker build -t "homeapi" .

# Launch the container
sudo docker run -d -p 6500:5000 --restart always --name homeapi homeapi


echo "Point your browser to 'http://<docker_host_ip>:6500/site/tami4setup' to get your API Key and configure the connection."
echo "After that, sending a GET request to 'http://<docker_host_ip>:6500/api/tami4/boil' will send the boil command to your Tami4 device."
echo 'Enjoy your HOT beverages!'

