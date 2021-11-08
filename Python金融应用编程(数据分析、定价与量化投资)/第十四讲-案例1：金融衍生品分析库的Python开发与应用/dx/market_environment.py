# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#market_environment.py

class market_environment(object):
    """
    这个类用来初始化用于估值的市场环境相关信息
    """
    def __init__(self,name,pricing_date):
        self.name=name
        self.pricing_date=pricing_date
        self.constants={}
        self.lists={}
        self.curves={}
    def add_constant(self,key,constant):
        self.constants[key]=constant
    def get_constant(self,key):
        return self.constants[key]
    def add_list(self,key,list_object):
        self.lists[key]=list_object
    def get_list(self,key):
        return self.lists[key]
    def add_curve(self,key,curve):
        self.curves[key]=curve
    def get_curve(self,key):
        return self.curves[key]
    def add_environment(self,env):
        """
        如果某个值是已经存在的，这里进行覆盖
        """
        for key in env.constants:
            self.constants[key]=env.constants[key]
        for key in env.lists:
            self.lists[key]=env.lists[key]
        for key in env.curves:
            self.curves[key]=env.curves[key]
    


