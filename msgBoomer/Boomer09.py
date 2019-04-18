import requests

phone = input("phone:")
url9 = 'https://www.lofter.com/lpt/getCaptcha.do?clientType=0&deviceType=pc&phone=' + phone + '&callback=loft.m.register.g.jsonpgetCaptcha'
header9 = {
    'Host': 'www.lofter.com', 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://www.lofter.com/phoneAccount/register',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Cookie': 'firstentry=%2FphoneAccount.do%3Fop%3Dregister%26X-From-ISP%3D2|; usertrack=ezq0pFvHNisnwvDtChUlAg==; JSESSIONID-WLF-XXD=19aaad835979f4c067f2f4b34933fc725b2321583a821c66b0d3132c3ee6139fc1a94deaadea4d03b1fd090edc6a64292df7d2cd926f8e8fbcd5b55877b5c758942589f8d365c1035e731843de1fc9019c7beeb27c5d655e2a9926cf2463e92e0b591ceba70f7a318c216a9bd37ca638c1a6a8a3f0c5cf2401834216e9424d164e23bea0; _ga=GA1.2.746225178.1539782189; _gid=GA1.2.1145748234.1539782189; __utma=61349937.746225178.1539782189.1539782189.1539782189.1; __utmc=61349937; __utmz=61349937.1539782189.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ntes_nnid=3ba5176bd3ecc7d189f54dfd98042658,1539782189894; NTESwebSI=0A0E0504FC0C68795AC9712E3A2E5BD3.hzabj-lofter-new14.server.163.org-8010; _gat=1; __utmb=61349937.2.10.1539782189'

}
data9 = ''
try:
    res9 = requests.get(url=url9, headers=header9)
    print(res9.content)
    print("susccess!")
except Exception as e:
    print("failed!")
    print(e)
