import requests
import execjs
import time

# sign encryption
# 0750F82C2-D8F6-49F6-878C-1E7EBEBC8DA2 is const

ctx = execjs.compile(open('./MD5.js', 'r', encoding='utf-8').read())

# timestamp
t = int(time.time() * 1000)

sign_str = f"appId=5053&t={t}&cityCode=310100&pageIndex="+ str(1) + "&pageSize=12&categoryCode=122&order=0750F82C2-D8F6-49F6-878C-1E7EBEBC8DA2"

# Compute sign
sign = ctx.call("hex_md5", sign_str)

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://souke.xdf.cn',
    'referer': 'https://souke.xdf.cn/search?cityCode=310100&categoryCode=122',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sign': sign,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}

params = {
    'appId': '5053',
    't': t,
    'cityCode': '310100',
    'pageIndex': '1',
    'pageSize': '12',
    'categoryCode': '122',
    'order': '0',
}

api_response = requests.get('https://dsapi.xdf.cn/product/v2/class/search', headers=headers, params=params)
print(api_response.text)
