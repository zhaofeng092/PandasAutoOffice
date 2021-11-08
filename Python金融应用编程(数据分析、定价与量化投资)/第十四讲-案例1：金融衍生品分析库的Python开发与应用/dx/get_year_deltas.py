# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#get_year_deltas

import numpy as np

def get_year_deltas(date_list,day_count=365.):
    """
    返回以年的比例表示的日期间隔的列表
    """
    start=date_list[0]
    delta_list=[(date-start).days/day_count for date in date_list]
    return np.array(delta_list)

