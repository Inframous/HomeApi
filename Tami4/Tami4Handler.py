from Tami4EdgeAPI import Tami4EdgeAPI
from .ApiKey import API_KEY


def boil_water():
    edge = Tami4EdgeAPI(API_KEY)
    edge.boil_water()
