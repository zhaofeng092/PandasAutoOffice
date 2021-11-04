# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values(by='Number', inplace=True, ascending=False)
students.index = range(0, len(students))
print(students)

plt.bar(students['Field'], students['Number'], color='orange', width=0.7)
plt.xticks(students['Field'], rotation='90')
plt.title('International Student by Field', fontsize=16)
plt.xlabel('Field')
plt.ylabel('Number')
plt.tight_layout()
plt.show()
