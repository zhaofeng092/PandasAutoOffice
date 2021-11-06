# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values('Number', inplace=True, ascending=False)
print(students)
students.plot.bar(x='Field', y='Number', color='blue', title='International Students by Field')
plt.tight_layout()
plt.show()
