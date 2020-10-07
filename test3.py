#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-09-01 11:59:55
LastEditTime: 2020-10-06 14:53:36
Description: 在这里描述当前文档
FilePath: /code/test3.py
'''
import requests

url = "http://hq.sinajs.cn/list=sz000851"
res = requests.get(url)
print(res.text)











# import time
# import datetime
# import schedule
# from random import choice
# import random
#
#
#
#
# def job4():
#     print('Job4:每天下午17:17执行一次')
#     print('Job4-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#     # print('Job4-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#     li = ["哈哈", "呵呵", "嘿嘿"]
#     print(li[0])
#
#     print('------------------------------------------------------------------------')
#
#
#
# schedule.every(1).minutes.do(job4)
# # # schedule.every().day.at('17:17').do(job4)
# while True:
#         schedule.run_pending()
