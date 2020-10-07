#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-10-06 14:25:50
LastEditTime: 2020-10-07 11:56:38
Description: 在这里描述当前文档
FilePath: /undefined/Users/wuxian/Desktop/code/获取实时价格.py
'''
from urllib.request import urlopen
import requests
import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 5000)  # 最多显示数据的行数

# =======神奇的网址
# 返回一个股票的数据：http://hq.sinajs.cn/list=sz000851 ,修改股票代码
# 返回一串股票的数据：http://hq.sinajs.cn/list=sh600000,sz000003,sz000851,sz300124,sh600276
# 正常网址：https://fiance.sina.com.cn/realstock/company/sh600000/nc.shtml
stock_code_list = ['sh600000','sz000003','sz000851','sz300124','sh600276']

# str = input('以空格为间隔连续输入一个数组:')
# list1= [int(n) for n in str.split()]
# print(list1)
# inputContent = input('请输入股票代码，以空格隔开')
# stock_code_list = [ str(n) for n in inputContent.split()]
url = "http://hq.sinajs.cn/list=" + ",".join(stock_code_list)
print(url)
# =========抓取数据
content = urlopen(url).read().decode('gbk') # 使用自带的库，从网络上获取信息
#content = requests.get(url).text
# =========将数据转换成DataFrame
content = content.strip()  # 去掉文本前后的空格，回车等
data_line = content.split('\n')  # 每行是一个股票的数据
data_line = [i.replace('var hq_str_', '').split(',') for i in data_line]
df = pd.DataFrame(data_line, dtype='float')
# ========对DataFrame进行整理
df[0] = df[0].str.split('="')
df['股票代码'] = df[0].str[0].str.strip()
df['股票名称'] = df[0].str[-1].str.strip()
df['candle_end_time'] = df[30] + ' ' + df[31]  # 股票市场的K线，是普遍以当根k线结束时间来命名的
df['candle_end_time'] = pd.to_datetime(df['candle_end_time'])
rename_dict = {1: '开盘价', 2: '昨收盘价', 3: '收盘价', 4: '最高价', 5: '最低价', 6: '买1价', 7: '卖1价', 8: '成交量', 9: '成交额',
               32: '状态'}  # 自己去对比数据，会有新的返回值
# 其中amount单位是股，volume单位是元
df.rename(columns=rename_dict, inplace=True)
df['状态']=df['状态'].str.strip('";')
df = df[['股票代码', '股票名称', 'candle_end_time', '开盘价', '昨收盘价', '收盘价', '最高价', '最低价', '买1价', '卖1价', '成交量', '成交额', '状态']]
# =================考察退市、停牌股票
df = df[df['开盘价'] - 0 > 0.000001]
print(df)
