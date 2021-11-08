# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#valuation_mcs_american.py

import numpy as np

from valuation_class import valuation_class

class valuation_mcs_american(valuation_class):
    """
    这个类使用单一因素Monte Carlo模拟方法来计算任意
    支付的美式期权的价值
    """
    def generate_payoff(self,fixed_seed=False):
        try:
            strike = self.strike
        except:
            pass
        paths = self.underlying.get_instrument_values(fixed_seed=fixed_seed) 
        time_grid = self.underlying.time_grid
        try:
            time_index_start = int(np.where(time_grid == self.pricing_date)[0])
            time_index_end = int(np.where(time_grid == self.maturity)[0])
        except:
            print "Maturity date not in time grid of underlying."
        instrument_values = paths[time_index_start:time_index_end + 1]
        try:
            payoff = eval(self.payoff_func)
            return instrument_values, payoff, time_index_start, time_index_end
        except:
            print "Error evaluating payoff function."
    
    def present_value(self,accuracy=6,fixed_seed=False,bf=5,full=False):
         instrument_values, inner_values, time_index_start, time_index_end = \
            self.generate_payoff(fixed_seed=fixed_seed)
         time_list = \
            self.underlying.time_grid[time_index_start:time_index_end + 1]

         discount_factors = self.discount_curve.get_discount_factors(
                            time_list,dtobjects=True)

         V = inner_values[-1]
         for t in range(len(time_list) - 2, 0, -1):
            df = discount_factors[t,1] / discount_factors[t + 1,1] 
            rg = np.polyfit(instrument_values[t], V * df, bf)
            C=np.polyval(rg,instrument_values[t])
            V = np.where(inner_values[t] > C, inner_values[t], V * df)
         df = discount_factors[0,1] / discount_factors[1,1]
         result = np.sum(df * V) / len(V)
         if full:
            return round(result, accuracy), df * V
         else:
            return round(result, accuracy)
    
    

