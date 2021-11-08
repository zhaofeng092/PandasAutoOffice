# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
#sn_random_numbers.py

import numpy as np

def sn_random_numbers(shape,antithetic=True,moment_matching=True,fixed_seed=False):
    if fixed_seed:
        np.random.seed(1000)
    if antithetic:
        ran=np.random.standard_normal((shape[0],shape[1],shape[2]/2))
        ran=np.concatenate((ran,-ran),axis=2)
    else:
        ran=np.random.standard_normal(shape)
    if moment_matching:
        ran=ran-np.mean(ran)
        ran=ran/np.std(ran)
    if shape[0]==1:
        return ran[0]
    else:
        return ran



