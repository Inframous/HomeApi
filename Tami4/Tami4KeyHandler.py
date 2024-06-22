import os 
from Tami4EdgeAPI import Tami4EdgeAPI

## Create a file with an empty API Key variable
file_path = 'Tami4/api_key/ApiKey.py'
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write("API_KEY = ''\n")


## Function to request the otp before requesting the API key
def request_key(mobile_number):
    Tami4EdgeAPI.request_otp(mobile_number)

## Sending the OTP and writing the API key to a file.
def send_otp(otp_code, mobile_number):
    try:
        api_key = Tami4EdgeAPI.submit_otp(mobile_number, otp_code)
        file_content = f"API_KEY = '{api_key}'"
        save_directory = 'Tami4/api_key'
        os.makedirs(save_directory, exist_ok=True)
        
        file_path = os.path.join(save_directory, 'ApiKey.py')

        with open(file_path, 'w') as file:
            file.write(file_content)
        print("Successfully written ApiKey.py in /app/Tami4/ApiKey")
    
    except Exception as e:
        print(e)
        exit()
