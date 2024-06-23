from flask import Flask, request
import json, time, requests

# 載入 LINE Message API 相關函式庫
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

app = Flask(__name__)

# Colab 環境需要下面這三行，本機環境不需要
# port = "5000"
# public_url = ngrok.connect(port).public_url
# print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\" ")

# def earth_quake():
#     result = []
#     code = '你的 token'
#     try:
#         # 小區域 https://opendata.cwa.gov.tw/dataset/earthquake/E-A0016-001
#         url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}'
#         req1 = requests.get(url)  # 爬取資料
#         data1 = req1.json()       # 轉換成 json
#         eq1 = data1['records']['Earthquake'][0]           # 取得第一筆地震資訊
#         t1 = data1['records']['Earthquake'][0]['EarthquakeInfo']['OriginTime']
#         # 顯著有感 https://opendata.cwa.gov.tw/dataset/all/E-A0015-001
#         url2 = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={code}'
#         req2 = requests.get(url2)  # 爬取資料
#         data2 = req2.json()        # 轉換成 json
#         eq2 = data2['records']['Earthquake'][0]           # 取得第一筆地震資訊
#         t2 = data2['records']['Earthquake'][0]['EarthquakeInfo']['OriginTime']
        
#         result = [eq1['ReportContent'], eq1['ReportImageURI']] # 先使用小區域地震
#         if t2>t1:
#           result = [eq2['ReportContent'], eq2['ReportImageURI']] # 如果顯著有感地震時間較近，就用顯著有感地震
#     except Exception as e:
#         print(e)
#         result = ['抓取失敗...','']
#     return result

def weather(address):
    # try:
        API_KEY = 'e8fef5845478923a029a170937d3e487'
        city_query = address
        geo_arr = f'http://api.openweathermap.org/geo/1.0/direct?q={city_query},TW&limit=1&appid={API_KEY}'
        geo_res = requests.get(geo_arr)
        geo_loc_dt = geo_res.json()
        place = geo_loc_dt[0]
        lat = place["lat"]
        lon = place["lon"]
        name_in_zh = place["local_names"]["zh"]
        query = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}&lang=zh_tw'
        #url = [f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization={code}',
        #    f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization={code}']
        result = {}
        
        req = requests.get(query)   # 爬取目前天氣網址的資料
        data = req.json()
        data2 = data["main"]
        data_weather = data["weather"][0]
        #station = data['records']['Station']   # 觀測站
        city = data['name']  # 縣市
        country = data['sys']['country']    # 區域
        
                # 使用「縣市+區域」作為 key，例如「高雄市前鎮區」就是 key
                # 如果 result 裡沒有這個 key，就記錄相關資訊
        if not f'{city}{country}' in result:
            weather = data_weather['main']
            weather_desc = data_weather['description']
            temp = round(data2['temp'])
            humid = data2['humidity']
            feels_like = data2["feels_like"]
            # 回傳結果
            result[f'{city} {country}'] = f'目前天氣狀況「{weather_desc}」，溫度 {temp} 度，相對濕度 {humid}% 體感溫度 {feels_like}！'
            

        output = '找不到氣象資訊'
        for i in result:
            if i in address: # 如果地址裡存在 key 的名稱
                output = f'「{address}」{result[i]}'
                print(output)
    #             break
    # except Exception as e:
    #     print(e)
    #     output = '抓取失敗...'
    # return output
Test = input("Enter a City\n")
print(weather(Test))
# access_token = '你的 Access Token'
# channel_secret = '你的 Channel Secret'

# @app.route("/", methods=['POST'])
# def linebot():
#     body = request.get_data(as_text=True)                    # 取得收到的訊息內容
#     try:
#         line_bot_api = LineBotApi(access_token)     # 確認 token 是否正確
#         handler = WebhookHandler(channel_secret)    # 確認 secret 是否正確
#         signature = request.headers['X-Line-Signature']             # 加入回傳的 headers
#         handler.handle(body, signature)      # 綁定訊息回傳的相關資訊
#         json_data = json.loads(body)         # 轉換內容為 json 格式
#         reply_token = json_data['events'][0]['replyToken']    # 取得回傳訊息的 Token ( reply message 使用 )
#         user_id = json_data['events'][0]['source']['userId']  # 取得使用者 ID ( push message 使用 )
#         print(json_data)                                      # 印出內容
#         type = json_data['events'][0]['message']['type']
#         if type == 'text':
#             text = json_data['events'][0]['message']['text']
#             if text == '雷達回波圖' or text == '雷達回波':
#                 line_bot_api.push_message(user_id, TextSendMessage(text='馬上找給你！抓取資料中....'))
#                 img_url = f'https://cwaopendata.s3.ap-northeast-1.amazonaws.com/Observation/O-A0058-001.png?{time.time_ns()}'
#                 img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
#                 line_bot_api.reply_message(reply_token,img_message)
#             # elif text == '地震':
#             #     line_bot_api.push_message(user_id, TextSendMessage(text='馬上找給你！抓取資料中....'))
#             #     reply = earth_quake()
#             #     text_message = TextSendMessage(text=reply[0])
#             #     line_bot_api.reply_message(reply_token,text_message)
#             #     line_bot_api.push_message(user_id, ImageSendMessage(original_content_url=reply[1], preview_image_url=reply[1]))
#             else:          
#                 text_message = TextSendMessage(text=text)
#                 line_bot_api.reply_message(reply_token,text_message)
#         elif type == 'location':
#             line_bot_api.push_message(user_id, TextSendMessage(text='馬上找給你！抓取資料中....'))
#             address = json_data['events'][0]['message']['address'].replace('台','臺')  # 取出地址資訊，並將「台」換成「臺」
#             reply = weather(address)          
#             text_message = TextSendMessage(text=reply)
#             line_bot_api.reply_message(reply_token,text_message)
#     except Exception as e:
#         print(e)
#     return 'OK'                 # 驗證 Webhook 使用，不能省略

# if __name__ == "__main__":
#     app.run()