# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('C:/Temp/Users.xlsx')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=False)
print(users)

users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True)
plt.tight_layout()
plt.show()
