#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-07-24 20:15:31
LastEditTime: 2020-09-28 20:14:55
Description: 在这里描述当前文档
FilePath: /code/同步爬虫.py
'''
import requests
from lxml import etree
import re
import multiprocessing
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
# 原则：线程池处理的是阻塞且较为耗时的操作

url = "https://www.pearvideo.com/category_5"
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
list = tree.xpath('//ul[@id="categoryList"]/li')
urls = []  # 存储所有视频的链接
for i in list:
    detail_url = 'https://www.pearvideo.com/' + i.xpath("./div/a/@href")[0]
    name = i.xpath("./div/a/div[2]/text()")[0] + ".mp4"
    print(detail_url, name)
    # 对详情页发出请求
    text2 = requests.get(url=detail_url, headers=headers).text
    # 从详情页中解析出视频的地址
    tree2 = etree.HTML(text2)
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, text2)[0]
    dic = {
        'name':name,
        'url':detail_url,
    }
    urls.append(dic)

#  使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = multiprocessing.Pool(4)
pool.map()