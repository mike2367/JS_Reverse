import requests
import subprocess
from functools import partial #用来固定某个参数的固定值
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')
import execjs

# 接口p_sysapi后的号码会根据时间变化
url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1128"
with open('深征信数据服务平台.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

accept_enkey = execjs.compile(jscode).call("window['indexcode'].getResCode")

data = {
"tdate": "2024-09-24",
"market": "SZE"
}
headers = {
"Referer":"https://webapi.cninfo.com.cn/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
"Cookie":"MALLSSID=544B31347346795A31575137337338442F4D386953397875452F36494A646B43636356354359674C4B64336550502F3332303034777A57747059737431474956; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1721184390,1721796880,1721870245; HMACCOUNT=9C1666AEF16C9008; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1721887896",
"Accept-Enckey": accept_enkey
}

response = requests.post(url, headers=headers, data=data).text
print(response)