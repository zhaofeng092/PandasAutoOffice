# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#valueation_mcs_european.py
import numpy as np
from valuation_class import valuation_class

class valuation_mcs_european(valuation_class):
    """
    对任意支付的欧式期权进行定价
    """
    def generate_payoff(self,fixed_seed=False):
        try:
            strike=self.strike
        except:
            pass
        paths=self.underlying.get_instrument_values(fixed_seed=fixed_seed)
        time_grid=self.underlying.time_grid
        try:
            time_index=np.where(time_grid==self.maturity)[0]
            time_index=int(time_index)
        except:
            print "Maturity date not in time_grid of underlying."
        maturity_value=paths[time_index]
        mean_value=np.mean(paths[:time_index],axis=1)
        max_value=np.amax(paths[:time_index],axis=1)[-1]
        min_value=np.amin(paths[:time_index],axis=1)[-1]
        
        try:
            payoff=eval(self.payoff_func)
            return payoff
        except:
            print "Error evaluating payoff function"
    
    def present_value(self,accuracy=6,fixed_seed=False,full=False):
        cash_flow=self.generate_payoff(fixed_seed=fixed_seed)
        discount_factor=self.discount_curve.get_discount_factors((
        self.pricing_date,self.maturity))[0,1]
        result=discount_factor*np.sum(cash_flow)/len(cash_flow)
        if full:
            return round(result,accuracy),discount_factor*cash_flow
        else:
            return round(result,accuracy)
    
    
        

