# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('C:/Temp/Orders.xlsx', index_col='Week')
print(weeks)

# weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
plt.title('Sales Trends', fontsize=16, fontweight='bold')
plt.xticks(weeks.index, fontsize=8)
plt.show()
