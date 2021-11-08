# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#plot_performance.py

import os.path

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__=="__main__":
    data=pd.io.parsers.read_csv(
        "equity.csv",header=0,
        parse_dates=True,index_col=0
    ).sort()
    fig=plt.figure()
    fig.patch.set_facecolor('white')
    
    ax1=fig.add_subplot(311,ylabel='Portfolio value: %')
    data['equity_curve'].plot(ax=ax1,color='blue',lw=2.)
    plt.grid(True)
    
    ax2=fig.add_subplot(312,ylabel='Period returns,%')
    data['returns'].plot(ax=ax2,color='black',lw=2.)
    plt.grid(True)
    
    ax3=fig.add_subplot(313,ylabel='Drawdowns, %')
    data['drawdown'].plot(ax=ax3,color='red',lw=2.)
    plt.grid(True)
    
    plt.show()


