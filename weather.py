import os
from functions.get_weather import get_weather
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv('api_key')


city_name = input("Enter the name of city: ")
get_weather(city_name, api_key)
