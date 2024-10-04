# python 调用本地js代码进行js逆向
from Useragents import ua_list
import random
import requests
import subprocess
from functools import partial #用来固定某个参数的固定值
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')
import execjs
# 查看环境

# 本地运行
class Spider(object):
    def __init__(self):
        self.url = "https://www.endata.com.cn/API/GetData.ashx"

    def get_headers(self):
        return {
            "User-Agent": random.choice(ua_list),
            "accept": "application/json, text/plain, */*",
            "content-type": "application/x-www-form-urlencoded"
        }

    def get_json(self):
        headers = self.get_headers()
        data = {
           "year":2024,
            "MethodName": "BoxOffice_GetYearInfoData"
        }
        response = requests.post(url=self.url, headers=headers, data=data).text

        return response


    def parse_js(self, en_data):

        with open('艺恩.js', 'r', encoding='utf-8') as f:
            jscode = f.read()
        ctx = execjs.compile(jscode).call('webInstace.shell', en_data)
        print(ctx)

    def run(self):
        en_data = self.get_json()
        self.parse_js(en_data)

if __name__ == "__main__":
    spider = Spider()
    spider.run()

