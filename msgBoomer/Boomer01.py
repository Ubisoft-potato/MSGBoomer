import requests, time

phone = input("phone:")
data1 = {
    'action': 'auth',
    'step': '1',
    'mobile': phone}

header1 = {
    'Referer': 'http://bbs.mydigit.cn/registe.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url1 = 'http://bbs.mydigit.cn/registe.php?nowtime=' + str(int(time.time() * 1000)) + '&verify=ae064c93'

try:
    res1 = requests.post(url=url1, data=data1, headers=header1)
    print(res1.content)
    print("success!")
except Exception as e:
    print("failed!")
    print(e.reason)
