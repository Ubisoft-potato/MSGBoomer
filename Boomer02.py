import requests

phone = input("phone:")
data2 = {
    'MOBILENO': phone,
    'TEMP': 1
}
header2 = {
    'Referer': 'http://qydj.scjg.tj.gov.cn/reportOnlineService/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url2 = 'http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login'
try:
    res2 = requests.post(url=url2, data=data2, headers=header2)
    print(res2.content)
    print("success!")
except Exception as e:
    print("failed!")
    print(e.reason)
