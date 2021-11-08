# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#strategy.py

from __future__ import print_function

from abc import ABCMeta,abstractmethod
import datetime
try:
    import Queue as queue
except ImportError:
    import queue

import numpy as np
import pandas as pd

from event import SignalEvent

class Strategy(object):
    """
    Strategy类是一个抽象类，提供所有后续派生策略处理对象的接口。派生策略类的目标是
    对于给定的代码基于DataHandler对象生成的数据来生成Signal。
    这个类既可以用来处理历史数据，也可以用来处理实际交易数据。只需要将数据存放到
    数据队列当中
    """
    __metaclass__=ABCMeta
    
    @abstractmethod
    def calculate_signals(self):
        """
        提供一种计算信号的机制
        """
        raise NotImplementedError("Should implement calculate_signals()")



