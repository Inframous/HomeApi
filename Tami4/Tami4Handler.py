from Tami4EdgeAPI import Tami4EdgeAPI
from .api_key.ApiKey import API_KEY 



def boil_water():
    edge = Tami4EdgeAPI(API_KEY)
    edge.boil_water()

def list_drinks():
    edge = Tami4EdgeAPI(API_KEY)
    device = edge.get_device()
    results = {'drinks': [ drink.name for drink in device.drinks ]}
    return results

def make_drink(drink_index):
    print("Hello")
    edge = Tami4EdgeAPI(API_KEY)
    device = edge.get_device()
    edge.prepare_drink(device.drinks[drink_index])
    return device.drinks[drink_index].name

def get_tami4_info():
    edge = Tami4EdgeAPI(API_KEY)
    device = edge.get_device()
    water_quality = device.water_quality
    info = {
        # 'uv_last_replaced': water_quality.uv.last_replacement,
        'uvNextReplaceDate': water_quality.uv.upcoming_replacement,
        'uvInstalled': water_quality.uv.installed,
        'filterMilliLittersPassed': water_quality.filter.milli_litters_passed,
    }
    return info