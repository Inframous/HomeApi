# HomeApi - Personal Api for Home Assistant
In this project, we will deploy a Flask based API for personal use.
For the moment, its only ability is to send Tami4Edge machine a command to boil the water, thus being able to use in automations with Home Assistant or any other automation method via a GET request.

### Automatic Installation:
1. Open up a terminal session and paste: 
```curl -s https://raw.githubusercontent.com/Inframous/HomeApi/main/install.sh | bash```
2. Point your browser to ```http://<host_url>:<container_port>/site/tami4setup``` to configure your API Key.
  example url: ```http://192.168.1.10:8080/site/tami4setup```
  
### Manual Installation:
To install this on a local Docker container:
1. clone the repo and cd into the repo folder: 
```git clone https://github.com/Inframous/HomeApi.git```
```cd HomeApi```
2. Build the Docker image:
```sudo docker build -t "homeapi' .```
3. Launch the container:
```sudo docker run -d -p 8080:5000 --restart always --name homeapi homeapi```
4. Point your browser to ```http://<host_url>:<container_port>/site/tami4setup``` to configure your API Key.
  example url: ```http://192.168.1.10:8080/site/tami4setup```

### To use with Home Assistant
1. Add the following to your ```configuration.yaml```:
```
rest_command:
  tami4boil:
    url: "http://10.5.5.71:5000/api/tami4/boil"
```
2. Now you can create a button card, and attach the new service.
<img src="https://raw.githubusercontent.com/Inframous/HomeApi/main/images/ha.jpg" alt="Alt Text" width="75%">

