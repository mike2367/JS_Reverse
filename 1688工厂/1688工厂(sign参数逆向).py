# 查看发现数据位于js文件，需要sign
# 通过启动器查找sign所在的js文件
# d.token + "&" + i + "&" + g + "&" + c.data
import time
import subprocess
from functools import partial #用来固定某个参数的固定值
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')
import execjs
import requests
token = "ec2da3c8474829365a60d00007fe175e"
# 根据网站要求保留十三位， 初始10位
i = round(time.time() * 1000)
g = '12574478'
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=10166&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\"}"}'

# 可根据时间戳替换进行参数校验
sign_key = token + "&" + str(i) + "&" + g + "&" + data

with open('1688.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode).call('h', sign_key)

params = {
        "jsv": "2.6.1",
        "appKey": 12574478,
        "t": i, # 注意时间戳的一致性问题
        "sign": ctx,
        "v": 1.0,
        "type": "jsonp",
        "isSec": 0,
        "timeout": 20000,
        "api": "mtop.taobao.widgetService.getJsonComponent",
        "dataType": "jsonp",
        "jsonpIncPrefix": "mboxfc",
        "callback": "mtopjsonpmboxfc3"
}
params['data'] = data
url = "https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
"Referer": "https://sale.1688.com/",
"cookie":"cna=WBUeH1lL7mgCAXdO/RHeRVqa; xlly_s=1; hng=HK%7Czh-TW%7CHKD%7C344; lid=tb158864809; ali_apache_track=c_mid=b2b-22006388821039d30d|c_lid=tb158864809|c_ms=1; sgcookie=E100fXsAoAViTlRx41bHrFf%2F%2BcAeOrvdrvHOSTdJdmz07UiNhUHXgPdfuEtTb09JKO7WBU%2FElvT%2BUdhnMgnWERTNqMvwl%2F86DYxjxiY6aQK1aoMvEBLCs6jxUN3B5UhGIC2M; csg=73826c97; uc4=id4=0%40U2grEanGX%2Bd2aklLSGdF%2FTlTrMU8dRS7&nk4=0%40FY4PaQKh2CNSzJYbw0h9hZ2LLBRdtg%3D%3D; __cn_logon__=false; cookie2=1f51b3d7f296a5a9499926ffc4b22609; t=1a0e3ce359a9ae79726fdd4646b7a557; _tb_token_=fdea8e96735e0; mtop_partitioned_detect=1; _m_h5_tk=ec2da3c8474829365a60d00007fe175e_1721707232793; _m_h5_tk_enc=b93276b3a7ed1ee8066928dab205fff5; tfstk=f-htCGZeXHxMTx9m1V9nobcD_bYn6f3wvcu5ioqGhDnKlmFmIqw1dwaaxfqiS56YMmg7jrXg1oFxz0ngj-XipZ3rvSmxuFzbcmiYmAvHZVuagStukQAo7q1WvrcTGi0Qr2FmH3AkZV9_7S0BqERpQ8EYlSa_hlZBJz47cSa_CeEQkzWffmNXJ2ZUorZblsaCOzUcCjueok64csHvhV9cGgrCGsGBgRE-5tffGXUTBjg_vvDn9PeTVJYfhpGsxqGi_JJddSunemHjVHXgfYU-v8D921n-bri8sXj6RSwjKY2tph1Yxf4YFSwdlsgLtvex97O5vykISxGZXZCb7fcuHuyplsy0Ob2SFcQ2z2N_lmyri35afqgraYVJ6gztd4Fd4HhowavVquUcCeLd3ty_-q6hwOzf1ek4JuY9ntW4KLaLqeLd3ty_8yEk-bBV3Jv5.; isg=BCcnAo1FDaFPEoklzpxljU_7tlvxrPuOGHgHHPmUQ7bd6EeqAXyL3mXuCuj2ANMG"
}

response = requests.get(url,
                       headers = headers,
                       params=params).text
print(response)