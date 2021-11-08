# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ
"""
Created on Sun Jan 03 10:53:39 2016

@author: zhuto
"""

import pandas.io.data as web
import nitroplot as nplt

aapl=web.DataReader('aapl',data_source='yahoo')[['Open','Close']]

Cell("A1").df=aapl

nplt.figure(figsize=(8,4))
nplt.plot(Cell("A2").vertical,Cell("C2").vertical,label='AAPL')
nplt.legend(loc=0)
nplt.grid(True)
nplt.xticks(rotation=35)
nplt.graph()
save('dn_plot.xlsx')

