#接口有问题！！！！
import requests
phone = input("phone:")
data5 = {
    'action': 'register_code',
    'mobile': phone,
    'smstype': '0'
}
header5 = {
    'Host': 'www.hongniang.com',
    'Connection': 'keep-alive',
    'Content-Length': '49',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://www.hongniang.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.hongniang.com/account/register_new1/from/index',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Cookie': 'Hm_lvt_13345a0835e13dfae20053e4d44560b9=1539753859,1539764530,1539765622,1539785564; Hm_lpvt_13345a0835e13dfae20053e4d44560b9=1539785564; PHPSESSID=p36jqoh0cb6vv0tarrv1mv0ls6; CwCzwf_baseInfo=think%3A%7B%22sex%22%3A%221%22%2C%22year%22%3A%221985%22%2C%22month%22%3A%221%22%2C%22day%22%3A%221%22%2C%22workProvince%22%3A%22-1%22%2C%22workCity%22%3A%22-1%22%2C%22workDict%22%3A%22-1%22%2C%22marriage%22%3A%221%22%7D'
}
url5 = 'http://www.hongniang.com/ajax/send_sms_code'
try:
        res5 = requests.post(url=url5, data=data5, headers=header5)
        print(res5.content)
        print("success!")
except Exception as e:
        print("failed!")
        print(e)