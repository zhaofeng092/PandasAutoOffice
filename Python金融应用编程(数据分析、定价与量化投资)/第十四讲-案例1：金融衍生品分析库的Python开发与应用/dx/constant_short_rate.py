# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#consant_short_rate.py

from get_year_deltas import *

class constant_short_rate(object):
    """
    这个类用于短期利率的贴现
    """
    def __init__(self,name,short_rate):
        self.name=name
        self.short_rate=short_rate
        if short_rate<0:
            raise ValueError('Short rate negative.')
    
    def get_discount_factors(self,date_list,dtobjects=True):
        if dtobjects is True:
            dlist=get_year_deltas(date_list)
        else:
            dlist=np.array(date_list)
        dflist=np.exp(self.short_rate*np.sort(-dlist))
        return np.array((date_list,dflist)).T
    

