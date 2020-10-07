#!/usr/bin/env python
# coding=utf-8
'''
Author: wuxian
Date: 2020-09-22 15:07:18
LastEditTime: 2020-09-22 17:31:07
Description: 学习类方法私有属性，继承
FilePath: /code/类方法-3.py
'''
# 私有属性
# class Women:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18

#     def secret(self):
#         print("%s的年龄是%d" % (self.name, self.__age))


# xiaofang = Women("小芳")

#  继承
class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("eat")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡觉")


class Dog(Animal):
    def __init__(self):
        pass
    def bark(self):
        print("汪汪叫")
# 父类方法重写
class xiaotianquan(Dog):
    def bark(self):
        print("嘤嘤嘤")
        # 调用父类方法
        super().bark
        #增加子类的代码
        print("&^%&^%&")

xtq = xiaotianquan()
xtq.eat()
xtq.bark()
