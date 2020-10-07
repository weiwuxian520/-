#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-10-05 11:24:59
LastEditTime: 2020-10-05 20:27:49
Description: 在这里描述当前文档
FilePath: /code/pandasTest.py
'''
import pandas as pd
import tushare as ts

# 获取历史数据

# token= ts.set_token('myToken')
# pro = ts.pro_api()
# df = pro.daily(ts_code='000851.SZ', start_date='20170101', end_date='20171231')
# print(df)

data = ts.get_hist_data('000851')
dataText = pd.DataFrame(data)
dataText.to_csv('000851高鸿科技.csv')
df = pd.DataFrame(pd.read_csv('./000851高鸿科技.csv'))
df_new = df.rename(columns={"date": '日期', 'open': '开盘价', 'high': '最高价', 'close': '收盘价', 'low': '最低价', 'volume': '成交量', 'price_change': '价格变动',
                            'p_change': '涨跌幅', 'ma5': '5日均价', 'ma10': '10日均价', 'ma20': '20日均价', 'v_ma5': '5日均量', 'v_ma10': '10日均量', 'v_ma20': '20日均量', 'turnover': '换手率'})
df_new.to_csv('000851高鸿科技.csv', encoding='GBK')
print(df_new)
