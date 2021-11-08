# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
import math
import numpy as np
from time import time

np.random.seed(20000)
t0=time()

S0=100.0;K=105.0;T=1.0;r=0.05;sigma=0.2
M=50;dt=T/M;I=250000

S=np.zeros((M+1,I))
S[0]=S0
for t in range(1,M+1):
    z=np.random.standard_normal(I)
    S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*z)

C0=math.exp(-r*T)*np.sum(np.maximum(S[-1]-K,0))/I

tnp1=time()-t0

print C0
print tnp1

