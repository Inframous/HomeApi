# HomeApi - Personal Api for Home Assistant
In this project, we will deploy a Flask based API for personal use.
For the moment, its only ability is to send Tami4Edge machine a command to boil the water, thus being able to use in automations with Home Assistant or any other automation method via a POST request.


### Automatic Installation:
The installation uses port 6500, for a different port, use manual installation method.
1. Open up a terminal session and paste: 
```curl -s https://raw.githubusercontent.com/Inframous/HomeApi/main/install.sh | bash```. 
2. Point your browser to ```http://<docker_host_url>:6500/site/tami4setup``` to configure your API Key.
  example url: ```http://192.168.1.10:6500/site/tami4setup```
  
### Manual Installation:
To install this on a local Docker container:
1. clone the repo and cd into the repo folder: 
```git clone https://github.com/Inframous/HomeApi.git```
```cd HomeApi```
2. Build the Docker image:
```sudo docker build -t "homeapi' .```
3. Launch the container:
```sudo docker run -d -v ./api_key:/app/Tami4/api_key -p 6500:5000 --restart always --name homeapi homeapi```
4. Point your browser to ```http://<docker_host_url>:6500/site/tami4setup``` to configure your API Key.
  example url: ```http://192.168.1.10:6500/site/tami4setup```

Note: The API Key is writting in a file in /app/Tami4/api_key.<br> 
Bind a local folder to /app/Tami4/api_key in the container so you won't have to regenerate the api key every time you update or recreate the container. *This is being done in the `docker run` command in phase 3

### To use with Home Assistant
1. Add the following to your ```configuration.yaml```:
```
rest_command:
  tami4boil:
    url: "http://<docker_host_url>:<api_port>/api/tami4/boil"
```
2. Now you can create a button card, and attach the new service.
<img src="https://raw.githubusercontent.com/Inframous/HomeApi/main/images/ha.jpg" alt="Alt Text" width="75%">

### General Use
1. Send a POST request to ```http://<docker_host_url>:6500/api/tami4/boil``` to tell your Tami4Edge device to start boiling water.