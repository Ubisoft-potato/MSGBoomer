import requests
import json
phone = input("phone:")
data8 = {
    'service': 'zymk',
    'imgCode': '',
    'refresh': '0',
    'mobile': phone
}
header8 = {
    'Referer': 'https://www.zymk.cn/login.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url8 = 'https://www.zymk.cn/sendsms/'
try:
        res8 = requests.post(url=url8, data=data8, headers=header8)
        print(res8.content)
        print("success!")
except Exception as e:
        print("failed!")
        print(e)