# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#derivatives_position.py

class derivatives_position(object):
    """
    这个类对衍生品头寸进行建模
    """
    def __init__(self,name,quantity,underlying,mar_env,otype,payoff_func):
        self.name=name
        self.quantity=quantity
        self.underlying=underlying
        self.mar_env=mar_env
        self.otype=otype
        self.payoff_func=payoff_func
    
    def get_info(self):
        print "NAME"
        print self.name,'\n'
        print "QUANTITY"
        print self.quantity,'\n'
        print "UNDERLYING"
        print self.underlying,'\n'
        print "MARKET ENVIRONMENT"
        print "\n**Constants**"
        for key,value in self.mar_env.constants.items():
            print key,value
        print "\n**Lists**"
        for key,value in self.mar_env.lists.items():
            print key,value
        print "\n**Curves**"
        for key,value in self.mar_env.curves.items():
            print key,value
        print "\nOPTION TYPE"
        print self.otype,'\n'
        print "PAYOFF FUNCTION"
        print self.payoff_func
    

