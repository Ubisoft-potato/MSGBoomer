# 访问限时
import requests

phone = input("phone:")
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.fengjr.com/cn/act/201804-pc-TY1888.html?f=s0&c=1bl05jjjq-1&channel=1bl05jjjq-1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Cookie': 'CPS_1bl05jjjq-1_200289_534=t%3D1539780615700%26cu%3Dnocu%26mk%3Dnomk%7C%7Cfa.sogou.com%2F%26mt%3D0; _fjrclflag=1; fjr_channel_code=1bl05jjjq-1; JSESSIONID=94BCD9FE0484AA8A77EBE3F94D2B8AAD; __jsluid=04b8e9f045af57023db22cb052c22257; _ga=GA1.2.22042392.1539780616; _gid=GA1.2.305837834.1539780616; _gat=1; Qs_lvt_185296=1539780617; Qs_pv_185296=3726714589536066000; fjr_channel=1bl05jjjq-1; fjr_channel_date=1539780617304; fjr_ad_channel=1bl05jjjq-1; fjr_ad_channel_date=1539780617305; fjr_did=f0597b26-f336-40c0-8944-152f1825c8ad; fjr_vts=1; _fjrvts=1; fjr_fst=1539780617307; fjr_lst=1539780617307; fjr_vct=1539780617307; fjr_sqn=1; fjr_internal_ip=192.168.1.119; Hm_lvt_cca0837a014621d8d933a0b1b2cb0be5=1539780617; Hm_lpvt_cca0837a014621d8d933a0b1b2cb0be5=1539780617; first_ad_channel=1bl05jjjq-1; first_ad_date=1539780617956; current_ad_channel=1bl05jjjq-1; current_ad_date=1539780617956; aclt=1539780617304; acl=1bl05jjjq-1; aclc=1bl05jjjq-1'
}
url10 = 'https://www.fengjr.com/api/v2/user/loginRegister/captcha/text'
try:
    res10 = requests.post(url=url10, data=data10, headers=header10)
    print(res10.content.decode('utf-8'))
    print("success!")
except Exception as e:
    print("failed!")
    print(e)
