#!/bin/bash

# Set Container name
CONTAINER_NAME="homeapi"

# Set the location of API key file (Stores the API key from Tami4)
API_KEY_FOLDER="$HOME/.tami4apikey"

# Clone the repository
git clone https://github.com/Inframous/HomeApi.git
cd HomeApi || exit

# Build the Docker image
sudo docker build -t "homeapi" .


# Check if the container is running
if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    echo "Container '${CONTAINER_NAME}' is running. Stopping and removing it..."
    # Stop the container
    docker stop ${CONTAINER_NAME}
    # Remove the container
    docker rm ${CONTAINER_NAME}
    echo "Container '${CONTAINER_NAME}' stopped and removed."
else
    echo "Container '${CONTAINER_NAME}' is not running or does not exist."
fi

# Launch the container
mkdir -p $API_KEY_FOLDER
sudo docker run -d -v $API_KEY_FOLDER:/app/Tami4/api_key -p 6500:5000 --restart always --name homeapi homeapi


echo 'Point your browser to http://docker_host_ip:6500/site/tami4setup to get your API Key and configure the connection.'
echo 'After that, sending a GET request to http://docker_host_ip:6500/api/tami4/boil will send the boil command to your Tami4 device.'
echo "Remember, your API KEY is stored at $API_KEY_FOLDER:/app/Tami4/api_key/ApiKey.py. You may back it up or simply go over the setup again if need be."
echo 'Enjoy your HOT beverages!'

