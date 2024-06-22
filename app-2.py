from flask import Flask, request
import json, time, requests
app = Flask(__name__)
Test = "Tamshui"
API_KEY = 'e8fef5845478923a029a170937d3e487'
city_query = Test 
geo_arr = f'http://api.openweathermap.org/geo/1.0/direct?q={city_query},TW&limit=1&appid={API_KEY}'
geo_res = requests.get(geo_arr)
geo_loc_dt = geo_res.json()
place = geo_loc_dt[0]
lat = geo_loc_dt[0]["lat"]
lon = geo_loc_dt[0]["lon"]
print(place)
def a(address):
        
        query = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}&lang=zh'
        res = requests.get(query)
        data = res.json()
#print(a(Test))