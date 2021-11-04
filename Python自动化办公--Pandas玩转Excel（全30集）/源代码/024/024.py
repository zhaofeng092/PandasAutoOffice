# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('C:/Temp/Sales.xlsx', dtype={'Month': str, 'Revenue': float})
print(sales)

slope, intercept, r_value, p_value, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='red')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.show()
