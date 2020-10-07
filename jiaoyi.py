#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-07-09 01:58:50
LastEditTime: 2020-10-05 19:30:47
Description: 在这里描述当前文档
FilePath: /code/jiaoyi.py
'''
#获取行情
import pandas as pd
import time
import ccxt
from wxpy import *
import requests



huobimex = ccxt.huobipro()
limt = 500

currenttime = int(time.time()//60*60*1000)
sincetime = currenttime-limt*60*1000

data = huobimex.fetch_ohlcv(symbol='ETH/USDT', limit=500, since=sincetime)
df = pd.DataFrame(data)
df = df.rename(columns={0:'time',1:'open', 2:'high', 3:'low', 4:'收',5:'量'})
df['time'] = pd.to_datetime(df['time'],unit="ms")+pd.Timedelta(hours=7)
df = df.set_index('time',drop=True)
# df.to_csv('jiaoyi.csv')
print(df)

# bot = Bot(cache_path=True,console_qr=-2)
# #查找好友
# friend = bot.friends().search('✨Hi')[0]
# print(friend)
# friend.send("Hello world")
# @bot.register()#接受指定人的信息在当前括号里添加
# def print_others(msg):
#     print('收到的信息：-->',msg)



