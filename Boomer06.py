import requests
import json

phone = input("phone:")
data6 = {
    "phone": phone,
    "type": "1",
}
data6 = json.dumps(data6)
header6 = {
    'Content-Type': 'application/json',
    'Referer': 'http://www.sparke.cn/user/register',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url6 = 'http://api.sparke.cn/v3/base/sms'
try:
    res6 = requests.post(url=url6, data=data6, headers=header6)
    print(res6.content)
    print("success!")
except Exception as e:
    print("failed!")
    print(e.reason)
