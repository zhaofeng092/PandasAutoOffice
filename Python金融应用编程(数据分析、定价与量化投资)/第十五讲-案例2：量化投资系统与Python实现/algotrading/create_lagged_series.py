# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
#create_lagged_series.py

import datetime

import numpy as np
import pandas as pd
from pandas.io.data import DataReader

def create_lagged_series(symbol,start_date,end_date,lags=5):
    """
    这个函数创建一个pandas的DataFrame，存储某个来自于Yahoo财经的股票
    的以调整收盘价计算的收益，以及一系列滞后的收益，还包括交易量以及某一天
    变动的方向
    """
    ts=DataReader(
        symbol,"yahoo",
        start_date-datetime.timedelta(days=365),
        end_date
    )
    
    tslag=pd.DataFrame(index=ts.index)
    tslag["Today"]=ts["Adj Close"]
    tslag["Volume"]=ts["Volume"]
    
    for i in range(0,lags):
        tslag["Lag%s" % str(i+1)]=ts["Adj Close"].shift(i+1)
    
    tsret=pd.DataFrame(index=tslag.index)
    tsret["Volume"]=tslag["Volume"]
    tsret["Today"]=tslag["Today"].pct_change()*100.0
    
    for i,x in enumerate(tsret["Today"]):
        if(abs(x)<0.0001):
            tsret["Today"][i]=0.0001
    
    for i in range(0,lags):
        tsret[
            "Lag%s" % str(i+1)
        ]=tslag["Lag%s" % str(i+1)].pct_change()*100.0
    
    tsret["Direction"]=np.sign(tsret["Today"])
    tsret=tsret[tsret.index>=start_date]
    return tsret



