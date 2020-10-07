
import requests

url = "https://www.sogou.com/web?"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

keywords = input("输入一个关键词\n")
#添加get请求的参数
param = {
    "query":keywords
}

res = requests.get(url=url,params=param,headers=header)
code = res.status_code
res_text = res.content.decode()

if code == 200:
    print(code,"ok")
    print(res_text)
else:
    print(code,"notgood")

# 持久化存储
filename = keywords+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(res_text)
print('存储成功')



