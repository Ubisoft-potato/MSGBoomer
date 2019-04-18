import requests
import time

phone = input("phone:")
url_get3 = 'http://www.yifatong.com/Customers/getsms?rnd='
header3 = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Referer': 'http://www.yifatong.com/Lawyers/register'
}

url3 = url_get3 + ("%0.3f" % time.time()) + "&mobile=" + phone
data3 = ''
try:
    res3 = requests.get(url=url3, headers=header3)
    print(res3.content)
    print("success!")
except Exception as e:
    print("failed!")
    print(e.reason)
