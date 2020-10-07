import requests
import json
url = "https://fanyi.baidu.com/sug"
header = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
keywords = input("输入想翻译的文字 \n")
data = {
        "kw": keywords
    }
resp = requests.post(url=url, data=data, headers=header)
resp_dic = resp.json()
print(resp_dic)

#持久化存储
fn = keywords+'.html'
fp = open(fn,'w',encoding='utf-8')
json.dump(resp_dic,fp=fp,ensure_ascii=False)
print("ok")

