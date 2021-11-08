# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
from time import time
from math import exp,sqrt,log
from random import gauss,seed

seed(20000)
t0=time()
S0=100.0
K=100.
T=1.0
r=0.05
sigma=0.2
M=50
dt=T/M
I=250000

S=[]
for i in range(I):
    path=[]
    for t in range(M+1):
        if t==0:
            path.append(S0)
        else:
            z=gauss(0.0,1.0)
            St=path[t-1]*exp((r-0.5*sigma**2)*dt+sigma*sqrt(dt)*z)
            path.append(St)
    S.append(path)

C0=exp(-r*T)*sum([max(path[-1]-K,0) for path in S])/I

tpy=time()-t0
print C0
print  tpy
