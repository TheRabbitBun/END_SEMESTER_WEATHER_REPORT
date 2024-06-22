from flask import Flask, request
import json, time, requests
app = Flask(__name__)
address = "Taoyuan"
API_KEY = '646083d35d91118aea86eaf05ffad39a'
def a(address):
        city_query = address + ",TW"
        geo_arr = f'http://api.openweathermap.org/geo/1.0/direct?q={city_query},TW&limit=3&appid={API_KEY}'
        geo_json = geo_arr.json()
        lat = geo_arr["lat"]
        lon = geo_arr["lon"]
        query = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}&lang=zh'