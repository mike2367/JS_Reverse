# AES decryption
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import requests
import execjs
ctx = execjs.compile(open('./AES.js', 'r', encoding='utf-8').read())

# json.parse
# interceptors.response

response = requests.post('https://vapi.jinglingshuju.com/Data/getResearchReport').text
payload = {
    'postpage': 1,
    'num': 20,
    'report_type': '',
    'source': '',
    'report_date': '',
    'uid': 'undefined'
}
response = requests.post('https://vapi.jinglingshuju.com/Data/getResearchReport', data=payload).json()
data = response['data']
decrypted_data = ctx.call('decrypt_', data)
print(decrypted_data)
