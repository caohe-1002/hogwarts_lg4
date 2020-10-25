# -*- coding: utf-8 -*-
# @Time  :2020/10/25 9:43 下午
# @Author : caohe
# @File :XuZhu.py
from pythonshizhan2.homework2.TSTL import TongLao

'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
class XuZhu(TongLao):
    #竹只有一个read（念经）的方法
    def read(self):
        #每次调用都会打印“罪过罪过”
        print("罪过罪过")
        #继承父类的方法
        super().see_people("YQL")
        super().fight_zms()



xuzhu=XuZhu(100,100,1000,1000)
xuzhu.read()







