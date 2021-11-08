# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#performance.py

from __future__ import print_function

import numpy as np
import pandas as pd

def create_sharpe_ratio(returns,periods=252):
    """
    计算策略的Sharpe比率，基于基准为0，也就是假设无风险利率为0
    """
    return np.sqrt(periods)*(np.mean(returns)/np.std(returns))

def create_drawdowns(pnl):
    """
    计算PnL曲线的最大回撤（从最大收益到最小收益之间的距离），以及回撤的时间
    这里需要参数pnl_returns是一个pandas的Series
    """
    hwm=[0]
    idx=pnl.index
    drawdown=pd.Series(index=idx)
    duration=pd.Series(index=idx)
    
    for t in range(1,len(idx)):
        hwm.append(max(hwm[t-1],pnl[t]))
        drawdown[t]=(hwm[t]-pnl[t])
        duration[t]=(0 if drawdown[t]==0 else duration[t-1]+1)
    
    return drawdown,drawdown.max(),duration.max()

    
