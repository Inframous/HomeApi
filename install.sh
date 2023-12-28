#!/bin/bash

# Prompt user to enter a port between 5000 and 10000
read -p "Please select a port number between 5000 and 10000 to be used for the API container: " selected_port

# Validate the input
if [[ ! "$selected_port" =~ ^[5-9][0-9]{3}$|^[1-9][0-9]{4}$|10000$ ]]; then
    echo "Invalid port number. Please enter a valid port between 5000 and 10000."
    exit 1
fi

# Clone the repository
git clone https://github.com/Inframous/HomeApi.git
cd HomeApi || exit

# Build the Docker image
sudo docker build -t "homeapi" .

# Launch the container with the selected port
sudo docker run -d -p "$selected_port":5000 --restart always --name homeapi homeapi

echo "Container is running on port $selected_port."

echo 'Point your browser to "http://<docker_host_ip>:'"$selected_port"'/site/tami4setup" to get your API Key and configure the connection.'
echo 'After that, sending a GET request to "http://<docker_host_ip>:'"$selected_port"'/api/tami4/boil" will send the boil command to your Tami4 device.'
echo 'Enjoy your HOT beverages!'
