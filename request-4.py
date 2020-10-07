#-*- coding:utf-8 -*-

import requests
import json
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

kw = input("请输入餐厅关键字\n")
kp = input("请输入页数\n")
ks = input("请输入每页展示的数据量\n")
data = {
    "cname": kw,
    "pid": "",
    "keyword": "",
    "pageIndex": kp,
    "pageSize": ks
}

resp = requests.post(url=url,headers=header,data=data)
list_json = resp.content.decode()
print(list_json)
fn = kw+'.csv'
fp = open(fn,'w',encoding='utf-8')
json.dump(list_json,fp=fp,ensure_ascii=False)
print("ok")