# 考古加电商数据
import requests
import execjs

headers = {
    'authority': 'service.kaogujia.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # cookie string KGJ-Token, last 7 days
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJhdWQiOiIxMDAwIiwiaXNzIjoia2FvZ3VqaWEuY29tIiwianRpIjoiNjkzOTVlN2Q1MmRmNDI4Mzg3Yzg3ZTg2NjVlYjc4NDkiLCJzaWQiOjc1NjQ3NTUsImlhdCI6MTcyODcxNzE0NSwiZXhwIjoxNzI5MzIxOTQ1LCJid2UiOjAsInR5cCI6MX0.8EDqr2Un7q3gN_w9SMHQshq2FEgZvfY3F79i7CV5SNucEGnhebFkqt2m5UYod-tJbWSGnCVCHA00BEex4pH8nA',
    'content-type': 'application/json',
    'origin': 'https://www.kaogujia.com',
    'referer': 'https://www.kaogujia.com/',
    'sec-ch-ua': '"Chromium";v="115", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'version_code': '3.1',
}

params = {
    'limit': '50',
    'page': '1',
    'sort_field': 'inc_fans_count',
    'sort': '0',
}

json_data = {
    'type': 2,
    'date_code': 20241011,
    'period': 1,
    'lv1': 0,
}

response = requests.post(
    'https://service.kaogujia.com/api/rank/author/fans/increment',
    params=params,
    headers=headers,
    json=json_data,
).json()
data = response['data']
url = "/api/rank/author/fans/increment"

with open('AES.js', 'r', encoding='utf-8') as f:
    aes_js = f.read()

ctx = execjs.compile(aes_js)
decrypted_data = ctx.call('decrypt', url, data)



