import requests
import json
import ssl

phone = input("phone:")
data4 = json.dumps({
    "mobile": phone,
    "captcha_value": "",
    "captcha_hash": ""})
header4 = {
    'Referer': 'https://h5.ele.me/login/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url4 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
try:
    res4 = requests.post(url=url4, data=data4, headers=header4)
    print(res4.content)
    print("success!")
except Exception as e:
    print("failed!")
    print(e.reason)
