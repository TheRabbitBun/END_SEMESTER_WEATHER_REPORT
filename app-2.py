from flask import Flask, request
import json, time, requests, math
app = Flask(__name__)
Test = input("Enter a City:\n")
API_KEY = 'e8fef5845478923a029a170937d3e487'
city_query = Test 
geo_arr = f'http://api.openweathermap.org/geo/1.0/direct?q={city_query},TW&limit=1&appid={API_KEY}'
geo_res = requests.get(geo_arr)
geo_loc_dt = geo_res.json()
place = geo_loc_dt[0]
lat = place["lat"]
lon = place["lon"]
name_in_zh = place["local_names"]["zh"]
query = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}&lang=zh'
res = requests.get(query)
data = res.json()
data2 = data["main"]
weather = data["weather"][0]
temp = round(data2["temp"])
min_temp = round(data2["temp_min"])
high_temp = round(data2["temp_max"])
feels_like = round(data2["feels_like"])
humidity = data2["humidity"]
weather_sta = weather["main"]
print(data)
print(name_in_zh)

#print(a(Test))