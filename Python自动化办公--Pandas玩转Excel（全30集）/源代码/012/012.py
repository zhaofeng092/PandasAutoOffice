# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx', index_col='From')
print(students)

students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()
