# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#execution.py

from __future__ import print_function

from abc import ABCMeta,abstractmethod
import datetime
try:
    import Queue as queue
except ImportError:
    import queue

from event import FillEvent,OrderEvent

class ExecutionHandler(object):
    """
    ExecutionHandler抽象类处理由Portfolio生成的order对象与实际市场中发生的
    Fill对象之间的交互。
    这个类可以用于实际的成交，或者模拟的成交
    """
    __metaclass__=ABCMeta
    
    @abstractmethod
    def execute_order(self,event):
        """
        获取一个Order事件并执行，产生Fill事件放到事件队列中
        """
        raise NotImplementedError("Should implement execute_order()")

class SimulatedExecutionHandler(ExecutionHandler):
    """
    这是一个模拟的执行处理，简单的将所有的订单对象转化为等价的成交对象，不考虑
    时延，滑价以及成交比率的影响。
    """
    def __init__(self,events):
        self.events=events
    
    def execute_order(self,event):
        """
        简单的讲订单对象自动转化为成交对象，不考虑时延，滑价以及成交
        比率的影响
        """
        if event.type=='ORDER':
            fill_event=FillEvent(datetime.datetime.utcnow(),
                                 event.symbol,
                                 'ARCA',event.quantity,event.direction,None)
            self.events.put(fill_event)
    
