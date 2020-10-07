import requests
import json
url = "https://movie.douban.com/j/chart/top_list?"
header = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

}
typenum = input("请输入电影类型数字：23～30")
parameters = {
    "type": typenum,
    "interval_id": "100:90",
    "action": "",
    "start": "0",#从库中的第几部电影去取
    "limit": "20"#一次取出的个数
}



resp = requests.get(url,params=parameters,headers=header)
code = resp.status_code
print(code,resp.content.decode())

list_data = resp.json()

#持久化
fp=open('豆瓣.html','w',encoding='utf-8')

json.dump(list_data,fp=fp,ensure_ascii=False)
print("ok")