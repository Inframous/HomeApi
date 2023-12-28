import os 
from Tami4EdgeAPI import Tami4EdgeAPI


def request_key(mobile_number):
    Tami4EdgeAPI.request_otp(mobile_number)


def send_otp(otp_code, mobile_number):
    try:
        api_key = Tami4EdgeAPI.submit_otp(mobile_number, otp_code)
        file_content = f"API_KEY = '{api_key}'"
        work_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(work_dir, 'ApiKey.py')

        with open(file_path, 'w') as file:
            file.write(file_content)
        print("Succeffuly written apikey.py")
    
    except Exception as e:
        print(e)
        exit()
    
