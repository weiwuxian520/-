#-*- coding:utf-8 -*-
import requests

url = "https://pic.qiushibaike.com/system/avtnew/3069/30696093/thumb/20180815155044.jpg?imageView2/1/w/90/h/90"
#text 字符串 content 二进制 jaso()对象

img_data = requests.get(url=url).content

with open("qiutu.jpg",'wb') as fp:
    fp.write(img_data)