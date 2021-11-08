# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
#simulation_class.py

import numpy as np
import pandas as pd

class simulation_class(object):
    """
    提供模拟类的基础方法
    """
    def __init__(self,name,mar_env,corr):
        try:
            self.name=name
            self.pricing_date=mar_env.pricing_date
            self.initial_value=mar_env.get_constant('initial_value')
            self.volatility=mar_env.get_constant('volatility')
            self.final_date=mar_env.get_constant('final_date')
            self.currency=mar_env.get_constant('currency')
            self.frequency=mar_env.get_constant('frequency')
            self.paths=mar_env.get_constant('paths')
            self.discount_curve=mar_env.get_curve('discount_curve')
            try:
                self.time_grid=mar_env.get_list('time_grid')
            except:
                self.time_grid=None
            try:
                self.special_dates=mar_env.get_list('special_dates')
            except:
                self.special_dates=[]
            self.instrument_values=None
            self.correlated=corr
            if corr is True:
                self.cholesky_matrix=mar_env.get_list('cholesky_matrix')
                self.rn_set=mar_env.get_list('rn_set')[self.name]
                self.random_numbers=mar_env.get_list('random_numbers')
        except:
            print "Error parsing market environment"
    
    def generate_time_grid(self):
        start=self.pricing_date
        end=self.final_date
        #pandas date_range function,freq=B,business day,'W' week,'M' month
        time_grid=pd.date_range(start=start,end=end,freq=self.frequency).to_pydatetime()
        time_grid=list(time_grid)
        if start not in time_grid:
            time_grid.insert(0,start)
        if end not in time_grid:
            time_grid.append(end)
        if len(self.special_dates)>0:
            time_grid.extend(self.special_dates)
            time_grid=list(set(time_grid))
            time_grid.sort()
        self.time_grid=np.array(time_grid)
    
    def get_instrument_values(self,fixed_seed=True):
        if self.instrument_values is None:
            self.generate_paths(fixed_seed=fixed_seed,day_count=365.)
        elif fixed_seed is False:
            self.generate_paths(fixed_seed=fixed_seed,day_count=365.)
        return self.instrument_values
    

