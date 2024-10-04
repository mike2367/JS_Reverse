# python 调用本地js代码进行js逆向
from Useragents import ua_list
import random
import requests
import subprocess
from functools import partial #用来固定某个参数的固定值
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')
import execjs
# 查看环境
print(execjs.get().name)
# 本地运行
class Spider(object):
    def __init__(self):
        self.url = "https://wyiosapi.qmpsee.com/Web/getCaDetail"

    def get_headers(self):
        return {
            "User-Agent": random.choice(ua_list),
            "accept": "application/json, text/plain, */*",
            "content-type": "application/x-www-form-urlencoded"
        }

    def get_json(self):
        headers = self.get_headers()
        data = {
           "page": 1,
           "num": 20,
           "ca_uuid": "6ebfe0e93f175caa91993aaf31a170f1"
        }
        response = requests.post(url=self.url, headers=headers, data=data).json()
        en_data = response['encrypt_data']
        return en_data


    def parse_js(self, en_data):
        with open('qi_encode.js', 'r', encoding='utf-8') as f:
            jscode = f.read()
        ctx = execjs.compile(jscode).call('Kde', en_data)
        print(ctx)

    def run(self):
        en_data = self.get_json()
        self.parse_js(en_data)

if __name__ == "__main__":
    spider = Spider()
    spider.run()