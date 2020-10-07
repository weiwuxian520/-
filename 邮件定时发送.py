#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-09-19 10:33:32
LastEditTime: 2020-09-28 20:06:49
Description: 在这里描述当前文档
FilePath: /code/邮件定时发送.py
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  导入所需要的的第三方库
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import yagmail
import requests
from lxml import etree
import smtplib
import os
import threading


# 爬取地址
url = "http://wufazhuce.com/"
# 头部伪装
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
#  邮箱信息参数
mail_host = 'smtp.gmail.com'
mail_username = "weiwuxian1520@gmail.com"
mail_password = 'weishaojia520'
sender = mail_username  # 发送人


# receivers = input("请输入接收人地址")  # 接收人


# 获取每日一句的内容
def get_content():
    res = requests.get(url=url, headers=header).text
    tree = etree.HTML(res)
    text = tree.xpath(
        '//*[@id="carousel-one"]/div/div[1]/div[2]/div[2]/a/text()')
    for i in text:
        content = str(i)
        print(content)
        return content


# 获取每日一句的图片
def get_img():
    res = requests.get(url=url, headers=header).text
    tree = etree.HTML(res)
    img_src = tree.xpath('//*[@id="carousel-one"]/div/div[1]/a/img/@src')[0]
    img_data = requests.get(url=img_src, headers=header).content
    img_name = '1.bmp'
    # 持久化存储
    with open(img_name, 'wb') as fp:
        fp.write(img_data)
        print(img_src, img_name, '下载成功')

    return img_name


def sendnews():      
    content = get_content()
    img = get_img()
    yag = yagmail.SMTP(user=mail_username,
                       password=mail_password, host=mail_host)
    yag.send(to='729874377@qq.com', subject='每日小浪漫',
             contents=content, attachments=img)
    yag.send(to='478655650@qq.com', subject='每日一句',
             contents=content, attachments=img)
    print("开始发送,当前时间：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("发送成功")
    if os.path.exists(img):
        os.remove(img)


if __name__ == '__main__':
    try:
        #  创建定时任务的调度器对象
        scheduler = BlockingScheduler()
        start_time = input('请输入发送时间,格式为(请用英文输入法):xxxx-xx-xx xx:xx:xx\n')
        scheduler.add_job(sendnews, 'interval', days=1, start_date=start_time)
        print("开始运行", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        scheduler.start()
    except smtplib.SMTPException as e:
        os.remove("./1.bmp")
        print("发送失败:", e)
