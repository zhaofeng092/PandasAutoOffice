# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd

df = pd.DataFrame()
df.to_excel('001.xlsx')

df = pd.DataFrame({'id':[1,2,3],'name':['a','b','c']})
df.to_excel('001-data.xlsx')

df = pd.DataFrame({'id':[1,2,3],'name':['a','b','c']})
df = df.set_index('id')
df.to_excel('001-data-index.xlsx')