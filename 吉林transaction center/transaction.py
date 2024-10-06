
import requests
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
with open('transaction.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'text/xml; charset=utf-8',
    'Host': 'www.ccprec.com',
    'Origin': 'https://www.ccprec.com',
    'Referer': 'https://www.ccprec.com/projectSecPage/',
    'Sec-CH-UA': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
}
# 1 is the page number
payload = ctx.call('encrypt', 1)
response = requests.post(
    'https://www.ccprec.com/honsanCloudAct',
    headers=headers,
    data=payload
)
decrypted_data = ctx.call('decryptCode', response.text)
print(decrypted_data)


