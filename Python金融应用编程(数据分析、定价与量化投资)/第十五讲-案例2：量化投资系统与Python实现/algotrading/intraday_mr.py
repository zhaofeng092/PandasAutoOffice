# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#intrady_mr.py

from __future__ import print_function

import datetime

import numpy as np
import pandas as pd
import statsmodels.api as sm

from strategy import Strategy
from event import SignalEvent
from backtest import Backtest
from hft_data import HistoricCSVDataHandlerHFT
from hft_portfolio import PortfolioHFT
from execution import SimulatedExecutionHandler

from itertools import product

class IntradayOLSMRStrategy(Strategy):
    """
    使用普通最小二乘法进行rolling的线性回归来确定两只股票之间的对冲比例。
    接着计算时间序列的残差的zscore，来分析是否它落在上下限之间，然后
    进行配对交易，生成交易或退出的信号
    """
    def __init__(
        self,bars,events,strat_params_list
    ):
        self.bars=bars
        self.symbol_list=self.bars.symbol_list
        self.events=events
        self.strat_params_list=strat_params_list
        
        self.pair=['AREX','WLL']
        self.datetime=datetime.datetime.utcnow()
        
        self.long_market=False
        self.short_market=False
    
    def calculate_xy_signals(self,zscore_last):
        """
        计算实际的x和y的信号配对，传递给信号生成的程序
        """
        y_signal=None
        x_signal=None
        p0=self.pair[0]
        p1=self.pair[1]
        dt=self.datetime
        hr=abs(self.hedge_ratio)
        
        if zscore_last<=-self.strat_params_list['zscore_high'] \
        and not self.long_market:
            self.long_market=True
            y_signal=SignalEvent(1,p0,dt,'LONG',1.0)
            x_signal=SignalEvent(1,p1,dt,'SHORT',hr)
        if abs(zscore_last)<=self.strat_params_list['zscore_low']\
        and self.long_market:
            self.long_market=False
            y_signal=SignalEvent(1,p0,dt,'EXIT',1.0)
            x_signal=SignalEvent(1,p1,dt,'EXIT',1.0)
        if zscore_last>=self.strat_params_list['zscore_low']\
        and not self.short_market:
            self.short_market=True
            y_signal=SignalEvent(1,p0,dt,'SHORT',1.0)
            x_signal=SignalEvent(1,p1,dt,'LONG',hr)
        if abs(zscore_last)<=self.strat_params_list['zscore_high']\
        and self.short_market:
            self.short_market=False
            y_signal=SignalEvent(1,p0,dt,'EXIT',1.0)
            x_signal=SignalEvent(1,p1,dt,'EXIT',1.0)
        
        return y_signal,x_signal
    
    def calculate_signals_for_pairs(self):
        """
        基于均值回复策略来生成一组信号。计算两只股票的对冲比例，使用OLS来进行。
        """
        y=self.bars.get_latest_bars_values(
            self.pair[0],"close",N=self.strat_params_list['ols_window']
        )
        x=self.bars.get_latest_bars_values(
            self.pair[1],"close",N=self.strat_params_list['ols_window']
        )
        if y is not None and x is not None:
            if(len(y)>=self.strat_params_list['ols_window'] and \
            len(x)>=self.strat_params_list['ols_window']):
                self.hedge_ratio=sm.OLS(y,x).fit().params[0]
                spread=y-self.hedge_ratio*x
                zscore_last=((spread-spread.mean())/spread.std())[-1]
                y_signal,x_signal=self.calculate_xy_signals(zscore_last)
                if y_signal is not None and x_signal is not None:
                    self.events.put(y_signal)
                    self.events.put(x_signal)
    
    def calculate_signals(self,event):
        """
        基于市场数据计算SignalEvents
        """
        if event.type=='MARKET':
            self.calculate_signals_for_pairs()
    
if __name__=="__main__":
    csv_dir='.'
    symbol_list=['AREX','WLL']
    initial_capital=100000.0
    heartbeat=0.0
    start_date=datetime.datetime(2007,11,8,10,41,0)
    strat_lookback=[50,100,200]
    strat_z_entry=[2.0,3.0,4.0]
    strat_z_exit=[0.5,1.0,1.5]
    strat_params_list=list(product(
        strat_lookback,strat_z_entry,strat_z_exit
    ))
    strat_params_dict_list=[
        dict(ols_window=sp[0],zscore_high=sp[1],zscore_low=sp[2])
        for sp in strat_params_list
    ]
    
    backtest=Backtest(
        csv_dir,symbol_list,initial_capital,heartbeat,
        start_date,HistoricCSVDataHandlerHFT,SimulatedExecutionHandler,
        PortfolioHFT,IntradayOLSMRStrategy,strat_params_dict_list
    )
    backtest.simulate_trading()

        