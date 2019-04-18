import requests
import json

phone = input("phone:")
url7 = "http://www.028jiajiao.com/home/member/code.shtml"

header7 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Referer': 'http://www.028jiajiao.com/member/join.shtml'
}
data7 = {
    'mobile': phone,
    'type': 'join'
}
try:
    res7 = requests.post(url=url7, data=data7, headers=header7)
    print(res7.content)
    print("susccess!")
except Exception as e:
    print("failed!")
    print(e.reason)
