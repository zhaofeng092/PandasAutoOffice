# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd
from datetime import date

orders = pd.read_excel('C:/Temp/Orders.xlsx', dtype={'Date': date})
orders['Year'] = pd.DatetimeIndex(orders.Date).year
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt1 = pd.DataFrame({'Sum': s, 'Count': c})
pt2 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)

print(pt1)
print(pt2)
