# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
"""
Created on Sun Dec 27 08:52:13 2015

@author: zhuto
"""

def bsm_call_value(S0,K,T,r,sigma):
    from math import log,sqrt,exp
    from scipy import stats
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    d2=(log(S0/K)+(r-0.5*sigma**2)*T)/(sigma*sqrt(T))
    value=(S0*stats.norm.cdf(d1,0.0,1.0)-K*exp(-r*T)*stats.norm.cdf(d2,0,1))
    return value

def bsm_vega(S0,K,T,r,sigma):
    from math import log,sqrt
    from scipy import stats
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    vega=S0*stats.norm.cdf(d1,0.0,1.0)*sqrt(T)
    return vega

def bsm_call_imp_vol(S0,K,T,r,C0,sigma_est,it=100):
    for i in range(it):
        sigma_est-=((bsm_call_value(S0,K,t,r,sigma_est)-C0)/bsm_vega(S0,K,T,r,sigma_est))        
    return sigma_est


        